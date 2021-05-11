import speech_recognition
import datetime
from gtts import gTTS
import os
import time
import playsound
import pyttsx3
import json
import unidecode
import re
import common

def dateTimeFormat(text):
    result = re.findall("ngày [0-9]* tháng [0-9]* năm [0-9]{4}", text)
    for index in range(len(result)):
        temp = result[index]
        ngay = re.findall('ngày [0-9]*', temp)[0]
        ngay = ngay.replace('ngày ', '')
        thang = re.findall('tháng [0-9]*', temp)[0]
        thang = thang.replace('tháng ', '')
        nam = re.findall('năm [0-9]{4}', temp)[0]
        nam = nam.replace('năm ', '')
        temp = thang + '/' + ngay + '/' + nam
        text = text.replace(result[index], temp)
    result = re.findall('[0-9]*/[0-9]*/[0-9]{4}.*[0-9]*:[0-9]*', text)
    for index in range(len(result)):
        temp = result[index]
        date = re.findall('[0-9]*/[0-9]*/[0-9]{4}', temp)[0]
        time = re.findall('[0-9]*:[0-9]*', temp)[0]
        text = text.replace(result[index], date + ' ' + time)
    return(text)


def listen(language="vi"):
    ear = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic:
        ear.adjust_for_ambient_noise(mic)
        print(common.assistant+": Đang nghe...")
        audio = ear.listen(mic, phrase_time_limit=10)
    try:
        text = ear.recognize_google(audio, language=language)
    except:
        text = ""
    if(not len(text)==0):
        print(common.you +": "+text)
    text = dateTimeFormat(text)
    return text
def speack_quick(text):
    mouth = pyttsx3.init()
    voices = mouth.getProperty("voices")
    voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An'
    # for voice in voices:
    #     print("Voice: %s" % voice.name)
    #     print(" - ID: %s" % voice.id)
    #     print(" - Languages: %s" % voice.languages)
    #     print(" - Gender: %s" % voice.gender)
    #     print(" - Age: %s" % voice.age)
    #     print("\n")
    mouth.setProperty("voice", voices[0].id)
    newVoiceRate = 130
    mouth.setProperty('rate', newVoiceRate)
    print(common.assistant+": "+text)
    mouth.say(text)
    mouth.runAndWait()


def speack(text):
    if(len(text) == 0):
        text = "Xin lỗi! Tôi không hiểu bạn nói gì!"
    filename = "sound/"+"query"+".mp3"
    filename = unidecode.unidecode(filename)
    # if(not os.path.isfile(filename)):
    #     text2speech = gTTS(text=text, lang='vi')
    #     text2speech.save(filename)
    text2speech = gTTS(text=text, lang='vi')
    text2speech.save(filename)
    print(common.const.assistant+": "+text)
    playsound.playsound(filename)
    if(text == 'Tắt máy trong 5 giây'):
        common.shutdown(0)