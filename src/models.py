class Submission(dict):
    """Reddit submission object"""
    def __init__(self, id, title, ups, downs, author):
        self.__setitem__('id', id)
        self.__setitem__('title', title)
        self.__setitem__('ups', ups)
        self.__setitem__('downs', downs)
        self.__setitem__('author', author)

class Message(dict):
    """Groupme message object"""
    def __init__(self, bot_id, text):
        self.__setitem__('bot_id', bot_id)
        self.__setitem__('text', text)
