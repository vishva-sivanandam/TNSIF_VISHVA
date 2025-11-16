import pyautogui as pg
import time
import voice_assistant as vs
import message as me

page = "home"
mpage = "home"
find = 1

def comment(text):
    global page
    global mpage
    open = 0

    if ("open" in text):
        m=pg.locateOnScreen(r"files\come.png",confidence=.7)
        pg.moveTo(m)
        pg.click()
        mpage="comment"
        open += 1

    elif ("close" in text):
        m=pg.locateOnScreen(r"files\close.png",confidence=.8)
        pg.moveTo(m)
        pg.click()
        mpage = "reels"

    elif ("post" or "add" or "commnet"in text and open ==0):
        m=pg.locateOnScreen(r"files\come.png",confidence=.7)
        pg.moveTo(m)
        pg.click()
        mpage="comment"
        time.sleep(2)
        m=pg.locateOnScreen(r"files\acmt.png",confidence=.8)
        pg.moveTo(m)
        pg.click()
        type_find = text.find("comment")
        type_find += 8
        type = text[type_find:]
        pg.write(type)
        pg.press('enter')
    

def home(text):
    global page
    global mpage
    global find
    find = 1

    if ("message" in text or "chat" in text and "unread" not in text):
        m=pg.locateOnScreen(r"files\mess.png",confidence=.7)
        pg.moveTo(m)
        pg.click()
        mpage = "message"
        me.mes(text)

    elif ("reel" in text):
        if (mpage != "reels"):
            m=pg.locateOnScreen(r"files\reels.png")
            pg.moveTo(m)
            pg.click()
            mpage = "reels"

    elif ("search" in text):
        m=pg.locateOnScreen(r"files\search.png")
        pg.moveTo(m)
        pg.click()
        mpage = "serach"
        

    elif ("home" in text):
        m=pg.locateOnScreen(r"files\house.png")
        pg.moveTo(m)
        pg.click()
        mpage = "home"

    elif ("explore" in text):
        m=pg.locateOnScreen(r"files\exp.png")
        pg.moveTo(m)
        pg.click()
        mpage = "explore"

    elif ("notification" in text):
        m=pg.locateOnScreen(r"files\noti.png",confidence = .8)
        pg.moveTo(m)
        pg.click()
        mpage="notifications"

    elif ("sound" in text or "mute" in text or "volume" in text):
        m=pg.locateOnScreen(r"files\Screenshot 2023-09-07 000459.png",confidence=.7)
        pg.moveTo(m)
        pg.click()


    elif ("create" in text):
        m=pg.locateOnScreen(r"files\create.png")
        pg.moveTo(m)
        pg.click()
        mpage="create"

    elif ("setting" in text):
        m=pg.locateOnScreen(r"files\td.png")
        pg.moveTo(m)
        pg.click()
        time.sleep(2)
        m=pg.locateOnScreen(r"files\sett.png",confidence=.8)
        pg.moveTo(m)
        pg.click()
        mpage="settings"

    elif ("more" in text or "3 dot" in text or "three dot" in text):
        m=pg.locateOnScreen(r"files\td.png")
        pg.moveTo(m)
        pg.click()
        mpage="more"

    elif ("like" in text and( "dislike" not in text and "remove" not in text and "unlike" not in text)):
        m=pg.locateOnScreen(r"files\like.png")
        pg.moveTo(m)
        pg.click()
        
    elif ("dislike" in text or "unlike" in text or ("remove" in text and "like" in text)):
        m=pg.locateOnScreen(r"files\ulike.png")
        pg.moveTo(m)
        pg.click()
        
    elif ("share" in text):
        if ("close" in text):
            m=pg.locateOnScreen(r"files\close.png",confidence=.8)
            pg.moveTo(m)
            pg.click()
            page = "home"
        else:
            m=pg.locateOnScreen(r"files\share.png")
            pg.moveTo(m)
            pg.click()
            page="share"
            time.sleep(2)
            
            if ( "to" in text):
                type_find = text.find("to")
                type_find += 3
                type = text[type_find:]
                pg.write(type)
                time.sleep(2)
                m=pg.locateOnScreen(r"files\sselect.png",confidence=.9)
                pg.moveTo(m)
                pg.click()
                time.sleep(.3)
                m=pg.locateOnScreen(r"files\ssend.png",confidence=.9)
                pg.moveTo(m)
                pg.click()
                page="home"


    elif ("save" in text):
        if ("un" not in text):
            m=pg.locateOnScreen(r"files\save.png")
            pg.moveTo(m)
            pg.click()
            print(1)
        else:
            m=pg.locateOnScreen(r"files\usave.png")
            pg.moveTo(m)
            pg.click()

    elif ("comment" in text):
        comment(text)

    elif ("profile" in text):
        m=pg.locateOnScreen(r"files\profile.png",confidence = .8)
        pg.moveTo(m)
        pg.click()
        mpage="profile"
    elif ("next post" in text):
        m=pg.locateOnScreen(r"files\hnext.png",confidence=.7)
        pg.moveTo(m)
        pg.click()

    else:
        find = 0
        return





    
    












