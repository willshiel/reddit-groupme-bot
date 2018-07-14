import time
import secrets
import praw
import logging


reddit = praw.Reddit(client_id=secrets.CLIENT_ID, client_secret=secrets.CLIENT_SECRET, password=secrets.PASSWORD, user_agent=secrets.USER_AGENT, username=secrets.USERNAME)

for submission in reddit.subreddit('soccer').hot(limit=10):
    print(submission.title)