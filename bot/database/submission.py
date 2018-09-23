from secrets import CONNECTION_STRING
from config import get_base_logging_directory, CONFIG
from pymongo import MongoClient
import logging

logging.basicConfig(filename=get_base_logging_directory() + 'database.log',
                    level=logging.ERROR)


class SubmissionClient(object):

    def __init__(self, db='submission'):
        try:
            self.client = MongoClient(CONNECTION_STRING)
            self.db = self.client[CONFIG["db"]]
            self.db_name = db
        except:
            logging.error("Unable to connect to database", exc_info=True)
            self.client = None
            self.db = None

    def insert_submission(self, submission):
        try:
            submissions_collection = self.db[self.db_name]
            id = submissions_collection.insert_one(submission)
        except:
            logging.error("Unable to insert into db", exc_info=True)
            return None

    def get_submission_by_id(self, id):
        try:
            submissions_collection = self.db[self.db_name]
            return submissions_collection.find({"id": id})
        except:
            logging.error("Unable to get the submission from the db", 
                          exc_info=True)
            return None

    def get_all_submissions(self):
        try:
            submissions_collection = self.db[self.db_name]
            return [sub for sub in submissions_collection.find({})]
        except:
            logging.error("Unable to get the submissions from the db",
                          exc_info=True)
            return None

    def delete_submission_by_id(self, id):
        """be very careful using this!!!!"""
        return NotImplementedError