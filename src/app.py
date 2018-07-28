"""contains all back end application logic for the bot"""
from reddit_client import RedditClient
from collections import deque

class App(object):

    def start():
        reddit = None
        while True:
            if reddit = None:
                reddit = RedditClient()
            reddit.get_hot_submissions()
        time.sleep(5 * 60)