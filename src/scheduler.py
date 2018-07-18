import time
import logging
from reddit_client import make_request, get_reddit

reddit = get_reddit()

while True:
    logging.debug("Making request.")
    make_request(reddit)
    logging.debug("Waiting five seconds to make next request.")
    time.sleep(5 * 60)