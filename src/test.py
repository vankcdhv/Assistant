from threading import Thread
import time
import datetime
from entity import Reminder
from database import ReminderDB


class CheckRemind():
   def __init__(self):
      pass
   @staticmethod
   def run():
        reminderList = ReminderDB.getInstance().getAll()
        for i in range(0, len(reminderList)):
            print(reminderList[i][1])
            print(datetime.date.today()==reminderList[i][1])

CheckRemind.run()