from datetime import datetime


class Submission(dict):
    """Reddit submission object"""
    def __init__(self, id, title, ups, downs, author, url,
                 last_modified=datetime.now(), created=datetime.now()):
        self.__setitem__('id', id)
        self.__setitem__('title', title)
        self.__setitem__('ups', ups)
        self.__setitem__('downs', downs)
        self.__setitem__('author', author)
        self.__setitem__('url', url)
        self.__setitem__('lastModified', last_modified)
        self.__setitem__('created', created)


class Group(dict):
    def __init__(self, name, bot_id, created, last_modified, active):
        self.__setitem__('name', name)
        self.__setitem__('bot_id', bot_id)
        self.__setitem__('created', created)
        self.__setitem__('last_modified', last_modified)
        self.__setitem__('active', active)
