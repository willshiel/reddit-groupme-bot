"""this will be different depending on the environment the app is running in"""
CONFIG = {"profile": "will", "db": "bot_test"}


def get_base_logging_directory():
    if (CONFIG['profile'] == 'will'):
        return "/home/willy/Development/reddit-groupme-bot/logs/"
    else:
        return "/home/bot/"
