import random
import math
import urllib.request
from utils import rabbitmq

MAX_OBJ_FETCH = 15

def round_half_up(n):
    multiplier = 1
    return math.floor(n*multiplier + 0.5) / multiplier

def imgs_gen():
    with open('urls.txt') as urls:
        for url in urls:
            contents = str(urllib.request.urlopen(url).read())
            yield contents

if __name__ == '__main__':
    input_select = bool(round_half_up(random.uniform(0, 1)))
    if input_select:
        obj_type = 'ImgObj'
        print(obj_type)
        ig = imgs_gen()
        try:
            for i in range(0, MAX_OBJ_FETCH):
                print(next(ig))
        except StopIteration:
            print('no more images to fetch')
    else:
        obj_type = 'LogObj'
        print(obj_type)
