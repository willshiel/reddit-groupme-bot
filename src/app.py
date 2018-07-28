"""contains all back end application logic for the bot"""
from reddit_client import RedditClient
from database_client import DatabaseClient
from collections import deque
import logging

logging.basicConfig(filename='logs/reddit_client.log', level=logging.ERROR)

queue = deque(maxlen=100)
reddit = None
groupme_client = None
db = None

def start():
    while True:
        _instantiate_clients()
        hot_subs = reddit.get_hot_submissions()
        new_subs = _remove_duplicates(hot_subs)
        for sub in new_subs:
            db.insert_submission(sub)
            groupme_client.post_message(sub.title)
        
    time.sleep(5 * 60)

def _remove_duplicates(submissions):
    new_subs = []
    for submission in submissions:
        if submission['id'] not in deque:
            deque.append(submission['id'])
            new_subs.append(submission)
    
    return new_subs

def _instantiate_clients():
    try:
        if reddit == None:
            reddit = RedditClient()
        if db == None:
            db = DatabaseClient()
    except:
        logging.error("Could not instantiate clients.", exc_info=True)