import time
import secrets
import praw
import logging
from utils import convert_to_submission

logging.basicConfig(filename='logs/reddit_client.log', level=logging.ERROR)

class RedditClient(object):

    def __init__(self):
        try:
            self.reddit = praw.Reddit(
                client_id=secrets.CLIENT_ID, 
                client_secret=secrets.CLIENT_SECRET, 
                password=secrets.PASSWORD, 
                user_agent=secrets.USER_AGENT, 
                username=secrets.USERNAME
            )

        except:
            logging.error("Unable to connect to reddit", exc_info=True)


    def get_hot_submissions(self):
        hot_submissions = []
        try:
            for submission in self.reddit.subreddit('soccer').hot(limit=25):
                if submission != None:
                    if submission.ups > 5000:
                        hot_submissions.append(convert_to_submission(submission))
                else:
                    logging.debug("There were no posts that were over the threshold.", exc_info=True)
                
            
            return hot_submissions

        except:
            logging.error("Unable to get submissions", exc_info=True)
