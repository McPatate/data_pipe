import sys
import random
import math
import json
import base64
import urllib.request
from utils import rabbitmq

MAX_OBJ_FETCH = 3
rmq = rabbitmq.RMQHelper()

def round_half_up(n):
    multiplier = 1
    return math.floor(n*multiplier + 0.5) / multiplier

def imgs_gen():
    with open('urls.txt') as urls:
        for url in urls:
            words = url.split('/')
            h = words[-1]
            w = words[-2]
            try:
                contents = urllib.request.urlopen(url).read()
                yield (contents, h, w)
            except urllib.error.HTTPError:
                yield 'image fetching error'

def prepare_log_payload(log):
    payload = '{ ' + '"objType":"log", "message":"{}"'.format(log) + ' }'
    return payload

def prepare_image_payload(image, height, width):
    payload = '{ ' + '"objType":"img", "image":"{}", "height":"{}", "width":"{}"'.format(create_base64_string(image), height, width) + ' }'
    return payload

def receive_callback(ch, method, properties, body):
    message = prepare_log_payload(str(body, 'utf-8'))
    ch.basic_publish(
        exchange='',
        routing_key='processing_queue',
        body=message,
        properties=rmq.create_properties()
    )

def create_base64_string(string):
    ''' make the image's base64 hash sendable through RMQ by converting it to utf-8 string
    '''
    return base64.b64encode(string).decode('utf-8')

if __name__ == '__main__':
    input_select = bool(round_half_up(random.uniform(0, 1)))
    if input_select:
        chan = rmq.open_channel()
        ig = imgs_gen()
        try:
            for i in range(0, MAX_OBJ_FETCH):
                msg_content = next(ig)
                if msg_content == 'image fetching error':
                    chan.basic_publish(
                        exchange='',
                        routing_key='logging_queue',
                        body=prepare_log_payload(msg_content),
                        properties=rmq.create_properties()
                    )
                else:
                    chan.basic_publish(
                        exchange='',
                        routing_key='processing_queue',
                        body=prepare_image_payload(*msg_content),
                        properties=rmq.create_properties()
                    )
        except StopIteration:
            print('no more images to fetch')
        except:
            print('unexpected error')
            chan.close()
            sys.exit(1)
    else:
        chan = rmq.open_channel()
        chan.basic_consume(queue='logging_queue', on_message_callback=receive_callback)
        chan.start_consuming()
    print('Exiting...')
    sys.exit(0)
