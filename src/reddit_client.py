from secrets import PASSWORD
import logging
import requests
import requests.auth

logging.basicConfig(level=logging.WARN)

REDDIT_URL = "http://www.reddit.com/r/redditdev/new.json?sort=new"
USER_AGENT = "RedditGroupMeClient/0.1 by RaulBravo"

def get_auth_token():
    client_auth = requests.auth.HTTPBasicAuth('8W0rxUUWJV6rHg', 'GKiyEej3EaC3OXtKsyXisI4vt70')
    post_data = {"grant_type": "password", "username": "raulbravo", "password": PASSWORD}
    headers = {"User-Agent": USER_AGENT}
    response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
    return response


def make_request():
    '''
        Makes the official request to the reddit api
        in order to get the 15 most popular posts
    '''
    auth_token = get_auth_token().json()
    headers = {'Authorization': 'bearer {}'.format(auth_token['access_token']), 'User-Agent': USER_AGENT}
    logging.warn(headers)
    response = requests.get(REDDIT_URL, headers=headers).json()
    logging.warn("This is the response: {}".format(response))

make_request()