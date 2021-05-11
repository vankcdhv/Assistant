import psutil
import os
import json
import time
import signal


def openSW(name, cmd=None):
    if(cmd != None):
        print(name + ' - ' + cmd)
    else:
        print(name)
    if(cmd == None):
        os.system('open -a ' + name + '')
    else:
        os.system('open -a ' + name + ' ' + cmd)


def closeSW(name):
    # Task in window
    # for process in (process for process in psutil.process_iter() if process.name() == (name+".exe").lower() or process.name() == (name+".exe").upper()):
    #     process.kill()
    # Task in Macos
    os.system('pkill "' + name + '"')


def shutdown(time):
    os.system('shutdown -s -t 5')
