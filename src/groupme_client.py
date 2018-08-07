import logging
import requests
from secrets import BOT_ID
from config import get_base_logging_directory
from utils import contains_url

logging.basicConfig(filename=get_base_logging_directory() + 'groupme.log',
                    level=logging.ERROR)


class GroupMeClient(object):

    def post_submission(self, sub):
        try:
            post = self._create_post(sub)
            r = requests.post("https://api.groupme.com/v3/bots/post",
                              data=post)
            if r.status_code != 202:
                raise RuntimeError("Unable to post groupme message.")
        except:
            logging.error("Unable to post message to groupme", exc_info=True)

    def _create_post(self, sub):
        post = {"bot_id": BOT_ID}
        if contains_url(sub):
            post['text'] = sub['title'] + '\n' + sub['url']
        else:
            post['text'] = sub['title']

        return post
