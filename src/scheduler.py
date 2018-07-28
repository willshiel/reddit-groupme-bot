import time
import logging
from reddit_client import RedditClient
from collections import deque

logging.basicConfig(filename='../logs/main.log', level=logging.ERROR)

def main():
    try:
        reddit = None
        while True:
            if reddit = None:
                reddit = RedditClient()
            hot_submissions = reddit.get_hot_submissions()
            time.sleep(5 * 60)
    except:
        logging.error("Error trying to connect to reddit", exc_info=True))
        logging.error("Bringing the bot down for a couple hours")
        time.sleep(5 * 60 * 60)

main()