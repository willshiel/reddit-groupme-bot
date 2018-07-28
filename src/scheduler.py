import time
import logging
from app import App

logging.basicConfig(filename='../logs/main.log', level=logging.ERROR)

def main():
    while True:
        try:
            App.start()
        except:
            logging.error("Error trying to connect to reddit", exc_info=True))
            logging.error("Bringing the bot down for a couple hours")
            time.sleep(5 * 60 * 60)

main()