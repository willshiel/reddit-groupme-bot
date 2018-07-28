from models import Submission
from pymongo import MongoClient
from secrets import CONNECTION_STRING
import logging

logging.basicConfig(filename='../logs/database.log', level=logging.ERROR)

class DatabaseClient(object):

    def __init__(self):
        try:
            self.client = MongoClient(CONNECTION_STRING)
            self.db = self.client['bot']    
        except:
            logging.error("Unable to connect to database", exc_info=True)
            self.client = None
            self.db = None

    def insertSubmission(self, submission):
        try:
            submissions_collection = self.db['submission']
            id = submissions_collection.insert_one(submission)
            if id is None:
                raise InsertError("Couldn't insert submission:\n{}".format(submission))
            return id
        except:
            logging.error("Unable to insert into db", exc_info=True)
            return None
        
    def getSubmissionById(self, id):
        try:
            submissions_collection = self.db['submission']
            return submissions_collection.find_one()
        except:
            logging.error("Unable to get the submission from the db", exc_info=True)
            return None

    def getAllSubmissions(self):
        try:
            submissions_collection = self.db['submission']
            return [sub for sub in submissions_collection.find({})]
        except:
            logging.error("Unable to get the submission from the db", exc_info=True)
            return None

    def deleteSubmissionById(self, id):
        """be very careful using this!!!!"""
        return NotImplementedError