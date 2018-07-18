import time
import secrets
import praw
import logging


def get_reddit():
    try:
        return praw.Reddit(
            client_id=secrets.CLIENT_ID, 
            client_secret=secrets.CLIENT_SECRET, 
            password=secrets.PASSWORD, 
            user_agent=secrets.USER_AGENT, 
            username=secrets.USERNAME
        )

    except:
        logging.error("Unable to connect to reddit")


def make_request(reddit):
    hot_submissions = []
    try:
        for submission in reddit.subreddit('soccer').hot(limit=25):
            if submission != None:
                if submission.ups > 5000:
                    hot_submissions.append(submission)
            else:
                logging.debug("There were no posts that were over the threshold.")
            
        
        return hot_submissions

    except:
        logging.error("Unable to get submissions")
