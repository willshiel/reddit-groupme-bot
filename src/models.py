class Submission(dict):
    """Reddit submission object"""
    def __init__(self, id, title, ups, downs, author, url):
        self.__setitem__('id', id)
        self.__setitem__('title', title)
        self.__setitem__('ups', ups)
        self.__setitem__('downs', downs)
        self.__setitem__('author', author)
        self.__setitem__('url', url)
