def equalIgnoreCase(s1, s2):
    return(s1.lower()==s2.lower())
def convertGoogleTimeToTime(text):
    text = text.split('+')[0]
    date = text.split('T')[0]
    time = text.split('T')[1]

    hour = time.split(':')[0]
    minute = time.split(':')[1]
    seconde = time.split(':')[2]

    ngay = date.split('-')[2]
    thang = date.split('-')[1]
    nam = date.split('-')[0]
    return hour, minute, seconde, ngay, thang, nam
