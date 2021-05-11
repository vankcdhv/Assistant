#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import speech_recognition
import datetime
from gtts import gTTS
import os
import time
import playsound
import pyttsx3
import json
import unidecode
import threading

import common
import apihandler as apiHandler
import solve
# from task import CheckRemind


def process(text):
    if common.equalIgnoreCase(text, ""):
        response = "Xin lỗi! Tôi không nghe rõ! Bạn nói lại được không?"
    elif common.equalIgnoreCase(text, "Hôm nay là thứ mấy"):
        response = "Hôm nay là " + \
            common.dayOfWeek[datetime.datetime.today().strftime('%A')]
    elif common.equalIgnoreCase(text, "Hôm nay là ngày mấy"):
        response = "Hôm nay là " + datetime.datetime.today().strftime("ngày %d tháng %m năm %Y")
    elif common.equalIgnoreCase(text, "Bây giờ là mấy giờ"):
        response = "Bây giờ là " + datetime.datetime.now().strftime("%H") + " giờ " + \
            datetime.datetime.now().strftime("%M")
    elif common.equalIgnoreCase(text, "Tắt máy"):
        response = "Tắt máy trong 5 giây"
    else:
        response = "Xin lỗi! Tôi không hiểu bạn nói gì!"
    return response


def startSession():
    while True:
        text = common.listen()
        if(not len(text) == 0):
            if(not common.equalIgnoreCase(text, "Tạm biệt")):
                response = ""
                if(len(text) > 0):
                    response = process(text)
                    if((''+response) == "Xin lỗi! Tôi không hiểu bạn nói gì!" or (''+response) == "Xin lỗi! Tôi không nghe rõ! Bạn nói lại được không?"):
                        response = apiHandler.process(text)
                        response = solve.solve(response, text)
                    common.speack(response)
                else:
                    response = "Xin lỗi! Tôi không hiểu bạn nói gì!"
                    common.speack(response)

            else:
                common.speack("Hẹn gặp lại!")
                break


while True:
    text = common.listen()
    if(common.equalIgnoreCase(text, 'Thức dậy nào') or common.equalIgnoreCase(text, 'Dậy nào')):
        common.speack('Chào Văn')
        startSession()
