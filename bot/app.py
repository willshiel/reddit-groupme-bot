"""contains all back end application logic for the bot"""
from clients.reddit_client import RedditClient
from clients.groupme_client import GroupMeClient
from database.submission import SubmissionClient
from database.group import GroupClient
from collections import deque
import time

submission_queue = deque(maxlen=100)
all_subs_over_150_queue = deque(maxlen=100)


def start():
    reddit = RedditClient()
    groupme_client = GroupMeClient()
    sub_db = SubmissionClient()
    data_db = SubmissionClient(db='learning_data')
    group_db = GroupClient()
    while True:
        hot_subs = reddit.submissions_upvoted_by_myself()
        new_subs = _remove_duplicates(hot_subs, submission_queue)
        all_subs_over_150 = reddit.submissions_over_n_upvotes(150)
        distinct_subs_over_150 = _remove_duplicates(all_subs_over_150, all_subs_over_150_queue)
        active_groups = group_db.get_all_active_groups()
        for group in active_groups:
            for sub in new_subs:
                sub_db.insert_submission(sub)
                groupme_client.post_submission(sub, group["bot_id"])

        for sub in distinct_subs_over_150:
            data_db.insert_submission(sub)

        time.sleep(5 * 60)


def _remove_duplicates(submissions, queue):
    new_subs = []
    for submission in submissions:
        if submission is not None and submission['id'] not in queue:
            queue.append(submission['id'])
            new_subs.append(submission)

    return new_subs
