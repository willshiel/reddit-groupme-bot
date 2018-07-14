import time
import secrets
import praw
import logging


def get_reddit():
    try:
        reddit = praw.Reddit(
            client_id=secrets.CLIENT_ID, 
            client_secret=secrets.CLIENT_SECRET, 
            password=secrets.PASSWORD, 
            user_agent=secrets.USER_AGENT, 
            username=secrets.USERNAME
        )

        return reddit
    except:
        logging.error("Unable to connect to reddit")


def make_request(reddit):
    logging.warning("made it here!")
    try:
        if reddit is None:
            reddit = get_reddit()
        for submission in reddit.subreddit('soccer').hot(limit=25):
            if submission != None:
                if submission.ups > 10000:
                    print(submission.title)
    except:
        logging.error("Unable to get submissions")
