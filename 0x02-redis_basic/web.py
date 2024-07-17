#!/usr/bin/env python3
'''jkhdssjijsxushouashaouwbahua aiuwe iouabwhwqhdhiqwbdiebakqwoushsousooa baoied 
'''
import redis
import requests
from functools import wraps
from typing import Callable

redis_store = redis.Redis()
'''gety a redis levek sinaotabce
'''

def data_cacher(method: Callable) -> Callable:
    '''GETS A LEVE SO FD SOUE SOUIDF BEYEK
    '''
    @wraps(method)
    def invoker(url) -> str:
        '''wrapper  zodf output 
        '''
        redis_store.incr(f'count:{url}')
        result = redis_store.get(f'result:{url}')
        if result:
            return result.decode('utf-8')
        result = method(url)
        redis_store.set(f'count:{url}', 0)
        redis_store.setex(f'result:{url}', 10, result)
        return result
    return invoker

@data_cacher
def get_page(url: str) -> str:
    '''cachign arequest request sdowyuwes dpweyhuenbkdfueb 
    '''
    return requests.get(url).text
