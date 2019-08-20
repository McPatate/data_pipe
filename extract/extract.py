import sys
import random
import math
import json
import base64
import urllib.request
from utils import rabbitmq

MAX_OBJ_FETCH = 15
rmq = rabbitmq.RMQHelper()

def round_half_up(n):
    multiplier = 1
    return math.floor(n*multiplier + 0.5) / multiplier

def imgs_gen():
    with open('urls.txt') as urls:
        for url in urls:
            contents = urllib.request.urlopen(url).read()
            yield contents

def prepare_payload(obj_type, message):
    payload = '{ ' + '"objType":"{}", "message":"{}"'.format(obj_type, message) + ' }'
    return payload

def receive_callback(ch, method, properties, body):
    obj_type = 'log'
    message = prepare_payload(obj_type, body)
    ch.basic_publish(
        exchange='',
        routing_key='processing_queue',
        body=message,
        properties=rmq.create_properties()
    )

if __name__ == '__main__':
    input_select = bool(round_half_up(random.uniform(0, 1)))
    if input_select:
        obj_type = 'img'
        chan = rmq.open_channel()
        ig = imgs_gen()
        try:
            for i in range(0, MAX_OBJ_FETCH):
                message = prepare_payload(obj_type, base64.b64encode(next(ig)).decode('utf-8'))
                chan.basic_publish(
                    exchange='',
                    routing_key='processing_queue',
                    body=message,
                    properties=rmq.create_properties()
                )
                print('sent msg : {}'.format(message))
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
