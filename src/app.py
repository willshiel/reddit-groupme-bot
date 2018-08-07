"""contains all back end application logic for the bot"""
from reddit_client import RedditClient
from database_client import DatabaseClient
from groupme_client import GroupMeClient
from collections import deque
from config import get_base_logging_directory
import time
import logging

logging.basicConfig(filename=get_base_logging_directory() + 'app.log',
                    level=logging.ERROR)

queue = deque(maxlen=100)


def start():
    reddit = None
    groupme_client = GroupMeClient()
    db = None
    print("Instantiating clients")
    while True:
        reddit, db = _instantiate_clients(reddit, db)
        hot_subs = reddit.get_hot_submissions()
        new_subs = _remove_duplicates(hot_subs)
        for sub in new_subs:
            print("inserting submissions")
            db.insert_submission(sub)
            print("posting messages")
            groupme_client.post_submission(sub)

        time.sleep(5 * 60)


def _remove_duplicates(submissions):
    new_subs = []
    for submission in submissions:
        if submission is not None and submission['id'] not in queue:
            queue.append(submission['id'])
            new_subs.append(submission)

    return new_subs


def _instantiate_clients(reddit, db):
    try:
        if reddit is None:
            reddit = RedditClient()
        if db is None:
            db = DatabaseClient()
        return (reddit, db)
    except:
        logging.error("Could not instantiate clients.", exc_info=True)
