import time
import logging
from app import start
from config import get_base_logging_directory

logging.basicConfig(filename=get_base_logging_directory() + 'scheduler.log',
                    level=logging.ERROR)


def main():
    while True:
        try:
            start()
        except:
            logging.error("Error trying to connect to reddit", exc_info=True)
            logging.error("Bringing the bot down for a couple hours")
            time.sleep(5 * 60 * 60)

main()
