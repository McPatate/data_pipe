import sys
import json
import base64
import hashlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
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

def create_json(obj):
    return '{ "objType":"img", "image":"' + '{}", "height":"{}", "width":"{}", "md5":"{}"'.format(create_base64_string(obj['image']), obj['height'], obj['width'], obj['md5']) + ' }'

def rgb2grey(rgb):
    return np.dot(rgb[...,:3], [0.3333, 0.3333, 0.3333])

def greyscale(img):
    img_obj = mpimg.imread(img)
    grey = rgb2grey(img_obj)
    plt.imshow(grey, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
    plt.savefig(img.split('.')[0] + '.png')

def prepare_image_payload(msg):
    img = decode_base64_string(msg['image'])
    msg['md5'] = hashlib.md5(img).hexdigest()
    # dirty fix
    with open('img_{}.jpeg'.format(msg['md5']), 'wb') as f:
        f.write(img)
    greyscale('img_{}.jpeg'.format(msg['md5']))
    print('img\'s md5 is {}'.format(msg['md5']))
    with open('img_{}.png'.format(msg['md5']), 'rb') as f:
        grey_img = f.read()
    msg['image'] = img
    return create_json(msg)

# def prepare_log_payload():

def clean_body(body):
    return str(body, 'utf-8').replace('\n', '')

def receive_callback(ch, method, properties, body):
    new_body = clean_body(body) 
    obj = json.loads(new_body)
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
