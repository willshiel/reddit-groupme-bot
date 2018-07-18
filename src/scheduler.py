import time
import logging
from reddit_client import make_request, get_reddit

reddit = get_reddit()

cached_posts = []

def add_submissions_to_cache(submissions):
    for submission in submissions:
        if submission not in cached_posts:
            cached_posts.append(submission)
            
        # make call to database here


def main():
    while True:
        logging.debug("Making request.")
        submissions = make_request(reddit)
        add_submissions_to_cache(submissions)
        logging.debug("Waiting five seconds to make next request.")
        time.sleep(5 * 60)

main()