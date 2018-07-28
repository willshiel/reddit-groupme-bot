import time
import logging
from reddit_client import make_request, get_reddit
from collections import deque
import pdb

# initialize logger
logging.basicConfig(filename='main.log', level=logging.ERROR)

submissions_cache = deque(maxlen=10)

def add_submissions_to_cache(submissions):
    for submission in submissions:
        pdb.set_trace()
        if submission.id not in submissions_cache:
            submissions_cache.appendleft(submission.id)

def main():
    try:
        reddit = get_reddit()
        while True:
            logging.debug("Making request.")
            submissions = make_request(reddit)
            add_submissions_to_cache(submissions)
            logging.debug("Waiting five seconds to make next request.")
            time.sleep(5 * 60)
    except:
        logging.error("Error trying to connect to reddit", exc_info=True))

main()