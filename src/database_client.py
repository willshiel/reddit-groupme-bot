from models import Submission
from pymongo import MongoClient
from secrets import CONNECTION_STRING
import logging
from config import get_base_logging_directory

logging.basicConfig(filename=get_base_logging_directory() + 'database.log', level=logging.ERROR)

class DatabaseClient(object):

    def __init__(self):
        try:
            self.client = MongoClient(CONNECTION_STRING)
            self.db = self.client['bot']    
        except:
            logging.error("Unable to connect to database", exc_info=True)
            self.client = None
            self.db = None

    def insert_submission(self, submission):
        try:
            submissions_collection = self.db['submission']
            id = submissions_collection.insert_one(submission)
            if id is None:
                raise InsertError("Couldn't insert submission:\n{}".format(submission))
            return id
        except:
            logging.error("Unable to insert into db", exc_info=True)
            return None
        
    def get_submissionById(self, id):
        try:
            submissions_collection = self.db['submission']
            return submissions_collection.find_one()
        except:
            logging.error("Unable to get the submission from the db", exc_info=True)
            return None

    def get_all_submissions(self):
        try:
            submissions_collection = self.db['submission']
            return [sub for sub in submissions_collection.find({})]
        except:
            logging.error("Unable to get the submission from the db", exc_info=True)
            return None

    def delete_submission_by_id(self, id):
        """be very careful using this!!!!"""
        return NotImplementedError