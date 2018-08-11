from bot.secrets import CLIENT_ID, CLIENT_SECRET, PASSWORD, USER_AGENT, USERNAME
import praw
import logging
from bot.utils import convert_to_submission
from bot.config import get_base_logging_directory

logging.basicConfig(filename=get_base_logging_directory() + 'reddit_client.log',
                    level=logging.ERROR)


class RedditClient(object):

    def __init__(self):
        try:
            self.reddit = praw.Reddit(
                client_id=CLIENT_ID,
                client_secret=CLIENT_SECRET,
                password=PASSWORD,
                user_agent=USER_AGENT,
                username=USERNAME
            )

        except:
            logging.error("Unable to connect to reddit", exc_info=True)

    def get_hot_submissions(self):
        hot_submissions = []
        try:
            for submission in self.reddit.subreddit('soccer').hot(limit=25):
                if submission is not None:
                    if submission.ups > 500:
                        hot_submissions.append(convert_to_submission(submission))
                else:
                    logging.debug("There were no posts that were over the threshold.",
                                  exc_info=True)

            return hot_submissions

        except:
            logging.error("Unable to get submissions", exc_info=True)
