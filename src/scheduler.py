from flask import Flask
import time
import atexit
import logging
import requests
import requests.auth
from secrets import PASSWORD

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

app = Flask(__name__)
logging.basicConfig(level=logging.WARN)

REDDIT_URL = "https://www.reddit.com/r/soccer/new/.json"
USER_AGENT = "RedditGroupMeClient/0.1 by RaulBravo"

def get_auth_token():
    client_auth = requests.auth.HTTPBasicAuth('8W0rxUUWJV6rHg', 'GKiyEej3EaC3OXtKsyXisI4vt70')
    post_data = {"grant_type": "password", "username": "raulbravo", "password": PASSWORD}
    headers = {"User-Agent": USER_AGENT}
    return requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)


def make_request(auth_token):
    '''
        Makes the official request to the reddit api
        in order to get the 15 most popular posts
    '''
    response = requests.get(REDDIT_URL).json()
    logging.warning(response)
    posts = response['data']['children']
    logging.warning(posts[0])

auth_token = get_auth_token()
make_request(auth_token)

scheduler = BackgroundScheduler()
scheduler.start()
scheduler.add_job(
    func=make_request,
    trigger=IntervalTrigger(minutes=5),
    id='reddit_request',
    name='Make request to /r/soccer every five minutes',
    replace_existing=True
)

atexit.register(lambda: scheduler.shutdown())