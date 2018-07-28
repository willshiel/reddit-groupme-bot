import logging
import requests

logging.basicConfig(filename='../logs/groupme.log', level=logging.ERROR)

class GroupMeClient(object):

    def post_message(self, message):
        try:
            r = requests.post("https://api.groupme.com/v3/bots/post", data=message)
            if r.status_code != 202:
                raise RuntimeError("Unable to post groupme message:\n{}".format(message))
        except:
            logging.error("Unable to post message to groupme", exc_info=True)