#!/usr/bin/env python3
"""Developing expiring web cache and tracker"""

from functools import wraps
import redis
import requests
from typing import Callable

redis_ = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """ Counter Decorator """
    @wraps(method)
    def wrapper(url):  # sourcery skip: use-named-expression
        """ Decorator Wrappe """
        redis_.incr(f"count:{url}")
        cached_html = redis_.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode('utf-8')
        html = method(url)
        redis_.setex(f"cached:{url}", 10, html)
        return html

    return wrapper


@count_requests
def get_page(url: str) -> str:
    """ It retrieves HTML content of URL  """
    req = requests.get(url)
    return req.text
