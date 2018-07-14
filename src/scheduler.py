import time
import logging
from reddit_client import make_request, get_reddit
import threading

reddit = get_reddit()

def call_reddit():
    t = threading.Timer(5.0, make_request, args=(reddit,))
    t.daemon = True
    t.start()

call_reddit()