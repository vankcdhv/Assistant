import mysql.connector


class DBContext:
    __instance = None

    @staticmethod
    def getInstance():
        if (DBContext.__instance == None):
            DBContext()
        return DBContext.__instance

    def __init__(self):
        if(DBContext.__instance == None):
            self.mydb = mysql.connector.connect(
                host="localhost",
                user='root',
                password='123456',
                database='assistant'
            )
            DBContext.__instance = self
    @property
    def mydb(self):
        return self.__mydb
    @mydb.setter
    def mydb(self, mydb):
        self.__mydb = mydb