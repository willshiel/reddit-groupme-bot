"""contains all back end application logic for the bot"""
from bot.clients.reddit_client import RedditClient
from bot.clients.groupme_client import GroupMeClient
from bot.database.submission import SubmissionClient
from bot.database.group import GroupClient
from collections import deque
import time

queue = deque(maxlen=100)


def start():
    reddit = RedditClient()
    groupme_client = GroupMeClient()
    sub_db = SubmissionClient()
    group_db = GroupClient()
    while True:
        hot_subs = reddit.get_hot_submissions()
        new_subs = _remove_duplicates(hot_subs)
        active_groups = group_db.get_all_active_groups()
        for group in active_groups:
            for sub in new_subs:
                sub_db.insert_submission(sub)
                groupme_client.post_submission(sub, group["bot_id"])

        time.sleep(5 * 60)


def _remove_duplicates(submissions):
    new_subs = []
    for submission in submissions:
        if submission is not None and submission['id'] not in queue:
            queue.append(submission['id'])
            new_subs.append(submission)

    return new_subs
