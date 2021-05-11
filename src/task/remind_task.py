from threading import Thread
import time
import datetime
from entity import Reminder
from database import ReminderDB

class CheckRemind(Thread):
    def __init__(self):
        super(CheckRemind, self).__init__()
    def run(self):
        while True:
            reminderList = ReminderDB.getInstance().getAll()
            for(i in range(0,len(reminderList))):

            time.sleep(60)