import mysql.connector
from .dbcontext import DBContext


class ReminderDB:
    __instance = None

    @staticmethod
    def getInstance():
        if(ReminderDB.__instance == None):
            ReminderDB()
        return ReminderDB.__instance

    def __init__(self):
        if(ReminderDB.__instance == None):
            self.__mydb = DBContext.getInstance().mydb
            ReminderDB.__instance = self

    def add(self, reminder):
        mycursor = self.__mydb.cursor()
        isRecordExisted = 0
        if(isRecordExisted == 1):
            sql = "UPDATE Calendar SET date = %s, time = %s, content = %s, isActive = %s WHERE ID = %s"
            val = (reminder.date, reminder.time, reminder.content,
                   reminder.isActive, reminder.id)
            mycursor.execute(sql, val)
            self.__mydb.commit()
            print(mycursor.rowcount, "record updated.")
        else:
            sql = "INSERT INTO Calendar(date, time, content, isActive) VALUES (%s, %s, %s, %s)"
            val = (reminder.date, reminder.time,
                   reminder.content, reminder.isActive)
            mycursor.execute(sql, val)
            self.__mydb.commit()
            print(mycursor.rowcount, "record inserted.")

    def getAll(self):
        mycursor = self.__mydb.cursor()
        sql = "SELECT * FROM Calendar"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        reminderList = []
        for row in myresult:
            reminderList.append(row)
        return reminderList
    def getByID(self, id):
        mycursor = self.__mydb.cursor()
        sql = "SELECT * FROM Calendar WHERE ID = " + str(id)
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        reminder = None
        for row in myresult:
            reminder = row
        return reminder
