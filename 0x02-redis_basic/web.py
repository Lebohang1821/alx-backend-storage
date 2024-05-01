#!/usr/bin/env python3
"""
Web Cache Module
"""
import redis
import requests
from functools import wraps
from typing import Callable

redis_store = redis.Redis()

def data_cacher(method: Callable) -> Callable:
    @wraps(method)
    def invoker(url) -> str:
        result = redis_store.get(f'result:{url}')
        if result:
            return result.decode('utf-8')
        try:
            response = requests.get(url)
            response.raise_for_status()
            result = response.text
            redis_store.incr(f'count:{url}')
            redis_store.setex(f'result:{url}', 10, result)
            return result
        except (requests.RequestException, redis.RedisError) as e:
            # Handle request or Redis errors
            print(f"Error fetching URL {url}: {e}")
            return ""
    return invoker

@data_cacher
def get_page(url: str) -> str:
    return requests.get(url).text

# Test the function
print(get_page("http://slowwly.robertomurray.co.uk/delay/5000/url/http://www.google.com"))
print(get_page("http://slowwly.robertomurray.co.uk/delay/5000/url/http://www.google.com"))
