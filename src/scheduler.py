from flask import Flask
import time
import atexit
import logging

from reddit_client import make_request, get_auth_token

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

app = Flask(__name__)

scheduler = BackgroundScheduler()
scheduler.start()

scheduler.add_job(
    func=make_request,
    trigger=IntervalTrigger(seconds=30),
    id='reddit_request',
    name='Make request to /r/soccer every five minutes',
    replace_existing=True
)

atexit.register(lambda: scheduler.shutdown())