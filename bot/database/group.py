import logging
from secrets import CONNECTION_STRING
from config import CONFIG
from pymongo import MongoClient

COLLECTION_NAME = "group_collection"


class GroupClient(object):

    def __init__(self):
        try:
            self.client = MongoClient(CONNECTION_STRING)
            self.db = self.client[CONFIG["db"]]
        except:
            logging.error("Unable to connect to database")
            self.client = None
            self.db = None

    def insert_group(self, group):
        try:
            groups_collection = self.db[COLLECTION_NAME]
            id = groups_collection.insert_one(group)
        except:
            logging.error("Unable to insert into db")
            return None

    def get_all_active_groups(self):
        try:
            groups_collection = self.db[COLLECTION_NAME]
            return [group for group in groups_collection.find({"active": True})]
        except:
            logging.error("Unable to get all groups from db")
            return None

    def get_group_by_name(self, name):
        try:
            groups_collection = self.db[COLLECTION_NAME]
            return groups_collection.find({"name", name})
        except:
            logging.error("Unable to get group from the db.")
