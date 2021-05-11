class Reminder:
    def __init__(self, id, date, time, content, isActive):
        self.id = id
        self.date = date
        self.time = time
        self.content = content
        self.isActive = isActive
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        self.__id = id
    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date):
        self.__date = date
    @property
    def time(self):
        return self.__time
    @time.setter
    def time(self, time):
        self.__time = time
    @property
    def content(self):
        return self.__content
    @content.setter
    def content(self, content):
        self.__content = content
    @property
    def isActive(self):
        return self.__isActive
    @isActive.setter
    def isActive(self, isActive):
        self.__isActive = isActive
    def __str__(self):
        return str(id) + ' | ' +  str(date) + ' | ' + str(time) + ' | ' + content + ' | ' + str(isActive)