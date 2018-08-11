import time
import logging
from bot.app import start


def main():
    while True:
        try:
            start()
        except:
            logging.error("Error trying to connect to reddit", exc_info=True)
            logging.error("Bringing the bot down for a couple hours")
            time.sleep(5 * 60 * 60)

main()
