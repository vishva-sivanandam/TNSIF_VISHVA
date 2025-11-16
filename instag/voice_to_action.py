import time
import pygetwindow as gw
import os
import voice_assistant as vs
import home
import reels_page as rp
import message as me
import user_monitor as usm
import display_data as dd
import threading
with open('data.txt', 'r') as file:
    path = file.read()

page = "null"
mpage = "null"
open = 0
feed = 0
timer = 0
find = 0

def check(text):
    print("processing:"+"*"+text+"*")

    if ("show" in text or "display" in text):
        display(text)
        return

    elif ("exit" in text):
        exit()
    windows_list = gw.getAllTitles()
    for i in windows_list:
        if ('Instagram' in i):
            global open
            global page
            open = 1
    if (open == 0):
        if ("open" not in text and "instagram" not in text or("close"in text and "instagram" in text)):
            vs.text_to_speech("can't process the action")
    if ("open" in text and "instagram" in text or open == 1):
        op(text)

def op(text):
    global page
    global open
    global feed
    global timer
    global find
    voice = 0
    page= home.mpage

    if ("timer" in text):
        if ("set" in text):
            timer = 1
            min = text.find("min")
            min = text[min-5:min]
            thread = threading.Thread(target=usm.timer,args=(min,))
            thread.start()
            vs.text_to_speech("instagram will be closed in"+str(min)+"minutes")
            return
        else:
            timer = 0
        
    elif ("open" in text and "instagram" in text):
        if (page == "null" or open == 0):
            os.startfile (path)
            window_title = 'Instagram'
            time.sleep(2)
            try:
                window= gw.getWindowsWithTitle(window_title)[0]
                window.maximize()
                find = 1
                page = "home"
            except IndexError:
                print("please maximize the Instagram window")
        else:
            vs.text_to_speech("instagram already opened")
            page = "home"
            return

    elif ("close" in text and "instagram" in text):
        window_title = 'Instagram'
        try:
            window= gw.getWindowsWithTitle(window_title)[0]
            window.close()
            find = 1
            page = "null"
            open = 0
            time.sleep(1)
        except IndexError:
            vs.text_to_speech("instagram is not opened")

    elif ("voice" and "feedback" in text):
        find = 1
        if (feed == 0):
            feed = 1
            voice = 1
            vs.text_to_speech("voice feedback enabled")

        else:
            feed = 0
            vs.text_to_speech("voice feedback disabled")

    elif (page != "null"):
        call_page(text)

    if find == 0:
        vs.text_to_speech(text+"  action not found")

    if (feed == 1 and voice == 0) and find ==1:
        vs.text_to_speech("processed"+text)



def display(t):
    if ("dashboard" in t):
        dd.dashboard()

    elif ("usage" in t and "time" in t):
        dd.usage_time()

    elif ("reels" in t and "count" in t):
        dd.reels_count()


def call_page(t):
    global page
    global mpage
    global find
    cpage = usm.page2

    if (cpage == "home"):
        home.home(t)
        find = home.find

    elif (cpage == "reels"):
        rp.reels(t)
        find = rp.find

    elif ("message" in cpage):
        me.mes(t)
        find = me.find
    if (find == 0 and cpage != "home"):
        home.home(t)
    print(cpage)


