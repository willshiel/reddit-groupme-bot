class Group(dict):
    def __init__(self, name, bot_id, created, last_modified, active):
        self.__setitem__('name', name)
        self.__setitem__('bot_id', bot_id)
        self.__setitem__('created', created)
        self.__setitem__('last_modified', last_modified)
        self.__setitem__('active', active)