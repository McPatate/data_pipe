import sys
import json
import base64
import hashlib
from utils import rabbitmq

rmq = rabbitmq.RMQHelper()

def create_base64_string(byte_string):
    ''' make the image's base64 hash sendable through RMQ by converting it to utf-8 string
    '''
    return base64.b64encode(byte_string).decode('utf-8')

def decode_base64_string(string):
    ''' transform base64 string back to byte then decode base64 to get image
    '''
    return base64.b64decode(string.encode('utf-8'))

def prepare_image_payload(msg):
    img = decode_base64_string(msg['image'])
    img_md5 = hashlib.md5(img).hexdigest()
    print('img\'s md5 is {}'.format(img_md5))
    with open('img_{}.jpeg'.format(img_md5), 'wb') as f:
        f.write(img)
    return '{ "hey":"ok" }'

# def prepare_log_payload():

def receive_callback(ch, method, properties, body):
    obj = json.loads(str(body, 'utf-8'))
    chan = rmq.open_channel()
    if obj['objType'] == 'img':
        payload = prepare_image_payload(obj)
    # else if obj['objType'] == 'log':
    #     payload = prepare_log_payload()
    chan.basic_publish(
        exchange='',
        routing_key='storing_queue',
        body=payload,
        properties=rmq.create_properties()
    )
    chan.close()

if __name__ == '__main__':
    chan = rmq.open_channel()
    chan.basic_consume(queue='processing_queue', on_message_callback=receive_callback)
    chan.start_consuming()
