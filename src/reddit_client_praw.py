import time
import secrets
import praw
import logging


r = praw.Reddit(client_id=secrets.CLIENT_ID,
                     client_secret=secrets.CLIENT_SECRET, password=secrets.PASSWORD,
                     user_agent=secrets.USER_AGENT, username=secrets.USERNAME)
r.login()

while True:
    subreddit = r.get_subreddit('soccer')
    for submission in subreddit.get_hot(limit=10):
        op_text = submission.selftext.lower()
        logging.warning(op_text)
    time.sleep(1800)