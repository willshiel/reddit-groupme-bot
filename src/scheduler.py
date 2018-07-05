from flask import Flask
import time
import atexit
import logging

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

app = Flask(__name__)
log = logging.getLogger(__name__)

def make_request():
    '''
        Makes the official request to the reddit api
        in order to get the 15 most popular posts
    '''
    log.debug("This is not yet implemented")
    print("This is not implemented yet.")
    return NotImplemented

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