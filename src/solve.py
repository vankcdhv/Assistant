import common
import json
import datetime

import apihandler as apiHandler
from entity import Reminder
# from database import ReminderDB


def solve(input, text):
    if(input.lower().startswith('thời tiết')):
        return apiHandler.getWeather(input)
    elif(input.lower().startswith('open')):
        name = input.split(' | ')[1]
        nameOri = input.split(' | ')[2]
        cmd = None
        try:
            cmd = input.split(' | ')[3]
        except:
            cmd = None
        common.openSW(name, cmd)
        return 'Okee! Mở ' + nameOri
    elif(input.lower().startswith('close')):
        name = input.split(' | ')[1]
        nameOri = input.split(' | ')[2]
        common.closeSW(name)
        return 'Okee! Đóng ' + nameOri
    elif(input.lower().startswith('song')):
        separator = input.split(' | ')[1]
        try:
            name = text.split(separator)[1]
        except:
            return 'Bài gì nhỉ?'
        url = apiHandler.youtube(name)
        if(url != None):
            common.openSW('safari', url)
            return 'Được thôi! Mở bài hát ' + name + ' trên youtube'
        else:
            return 'Không tìm thấy bài hát'
    elif(input.lower().startswith('google_search')):
        separator = input.split(' | ')[1]
        info = None
        try:
            info = text.split(separator)[1]
        except:
            pass
        if(info != None):
            url = 'https://www.google.com/search?q='+info
            url = url.replace(' ', '%20')
            common.openSW('safari', url)
            return 'Đây là thông tin về ' + info + ' được tìm kiếm trên google'
        else:
            return 'Bạn muốn tìm cái gì?'
    elif(input.lower().startswith('wiki_sumary')):
        separator = input.split(' | ')[1]
        info = None
        try:
            info = text.split(separator)[1]
        except:
            pass
        if(info != None):
            return apiHandler.wikipedia_sumary(info)
        else:
            return 'Bạn muốn tìm cái gì?'
    elif(input.lower().startswith('create remind')):
        array = input.split(' | ')
        content = array[1]
        hour, minute, second, ngay, thang, nam = common.convertGoogleTimeToTime(array[2])
        date = nam + '-' + thang + '-' + ngay
        time = hour + ':' + minute + ':00'
        isActive = True
        reminder = Reminder(0, date, time, content, isActive)
        # ReminderDB.getInstance().add(reminder)
        return 'Đã đặt lịch cho ' + content + ' vào ' + hour + ' giờ ' + minute + ' phút ngày ' + ngay + ' tháng ' + thang + ' năm ' + nam
    else:
        return input
