import pyautogui as pg
import time
import voice_assistant as vs
import pygetwindow as gw

mpage = "message"
page = "message"
find = 1

def mes(text):
    time.sleep(.8)
    global mpage
    global page
    global find

    if ("open" in text and "unread" in text):
        time.sleep(.5)
        m=pg.locateOnScreen(r"files\mnr.png",confidence=.9)
        pg.moveTo(m)
        pg.click()
        mpage="inside"
    
    elif("open message" in text):
        None

    elif ("send" in text and "to" in text):
        type_find = text.find("to")
        type_find += 3
        type = text[type_find:]
        m=pg.locateOnScreen(r"files\sendmm.png",confidence=.9)
        pg.moveTo(m)
        pg.click()
        time.sleep(.5)
        pg.write(type)
        time.sleep(2)
        m=pg.locateOnScreen(r"files\sselect.png",confidence=.9)
        pg.moveTo(m)
        pg.click()
        m=pg.locateOnScreen(r"files\chat.png",confidence=.9)
        pg.moveTo(m)
        pg.click()
        time.sleep(1)
        type_find1 = text.find("send")
        type_find1 += 5
        type_find = text.find("to")
        type_find -= 1
        type = text[type_find1:type_find]
        if ("message" in type):
            type = type.replace("message","")
        pg.write(type)
        pg.press('enter')
        page = page
        mpage = "inside"

    elif ("unread" in text and ("how" in text or "count" in text)):
        time.sleep(.3)
        m=pg.locateOnScreen(r"files\mcount.png",confidence=.9)
        if (m != None):
            pg.moveTo(m)
            pg.click()
            time.sleep(3)
            windows_list = gw.getAllTitles()
            for i in windows_list:
                if "Instagram" in i:
                    vs.text_to_speech("you have"+i[13]+"unread chats")
        else:
            vs.text_to_speech("you have no unread chats")


    elif ("home" in text):
        m=pg.locateOnScreen(r"files\house.png")
        pg.moveTo(m)
        pg.click()
        mpage = "home"
        page = "home"

    else:
        find = 0
        return


