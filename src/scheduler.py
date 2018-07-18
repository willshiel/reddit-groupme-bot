import time
import logging
from reddit_client import make_request, get_reddit


def main():
    reddit = get_reddit()
    while True:
        logging.debug("Making request.")
        submissions = make_request(reddit)
        add_submissions_to_cache(submissions)
        logging.debug("Waiting five seconds to make next request.")
        time.sleep(5 * 60)

main()