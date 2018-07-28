import logging
import requests
from secrets import BOT_ID

logging.basicConfig(filename='logs/groupme.log', level=logging.ERROR)

class GroupMeClient(object):

    def post_text_message(self, message):
        try:
            post = {"bot_id": BOT_ID, 'text': message}
            r = requests.post("https://api.groupme.com/v3/bots/post", data=post)
            if r.status_code != 202:
                raise RuntimeError("Unable to post groupme message:\n{}".format(message))
        except:
            logging.error("Unable to post message to groupme", exc_info=True)