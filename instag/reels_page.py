import pyautogui as pg
import time
import user_monitor as usm

page = "reels"
mpage = "reels"
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

def reels(text):
    global page
    global mpage
    global find
    global reels_count

    if ("unmute" in text):
        m=pg.locateOnScreen(r"files\runmute.png",confidence=.9)
        pg.moveTo(m)
        pg.click()

    elif ("mute" in text):
        m=pg.locateOnScreen(r"files\rmute.png",confidence=.9)
        pg.moveTo(m)
        pg.click()

    elif ("home" in text):
        m=pg.locateOnScreen(r"files\house.png")
        pg.moveTo(m)
        pg.click()
        mpage = "home"
        page = "home"

    elif ("comment" in text):
        comment(text)


    elif ("like" in text):
        pg.moveTo(x=1360, y=570)
        pg.click()

    elif ("share" in text):
        if ("close" in text):
            m=pg.locateOnScreen(r"files\close.png",confidence=.8)
            pg.moveTo(m)
            pg.click()
            mpage = "reels"
        else:
            m=pg.locateOnScreen(r"files\share.png",confidence=.9)
            pg.moveTo(m)
            pg.click()
            mpage="share"
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
                mpage="reels"
    
    elif ("save" in text):
        if ("un" not in text):
            m=pg.locateOnScreen(r"files\save.png")
            pg.moveTo(m)
            pg.click()
        else:
            m=pg.locateOnScreen(r"files\usave.png")
            pg.moveTo(m)
            pg.click()
    
    elif ("more" in text):
        m=pg.locateOnScreen(r"files\rmore.png")
        pg.moveTo(m)
        pg.click()
        mpage="more"
        if ("back" in text):
            mpage = "reels"
    
    elif ("follow" in text and ("account" in text or "id" in text)):
        if ("unfollow" in text):
            m=pg.locateOnScreen(r"files\rmore.png",confidence=.8)
            pg.moveTo(m)
            pg.click()
            time.sleep(1.5)
            m=pg.locateOnScreen(r"files\runfollow.png", confidence=.7)
            pg.moveTo(m)
            pg.click()
            time.sleep(1)
            m=pg.locateOnScreen(r"files\rmore.png",confidence=.8)
            pg.moveTo(m)
            pg.click()
        else:
            m=pg.locateOnScreen(r"files\rmore.png",confidence=.8)
            pg.moveTo(m)
            pg.click()
            time.sleep(1.5)
            m=pg.locateOnScreen(r"files\rfollow.png", confidence=.7)
            pg.moveTo(m)
            pg.click()
            time.sleep(1)
            m=pg.locateOnScreen(r"files\rmore.png",confidence=.8)
            pg.moveTo(m)
            pg.click()


    elif ("about" in text and "account"):
        if "close" in text:
            m=pg.locateOnScreen(r"files\aclose.png",confidence=.9)
            pg.moveTo(m)
            pg.click()
            time.sleep(.3)
            m=pg.locateOnScreen(r"files\rmore.png",confidence=.8)
            pg.moveTo(m)
            pg.click()
        else:
            m=pg.locateOnScreen(r"files\rmore.png",confidence=.8)
            pg.moveTo(m)
            pg.click()
            time.sleep(1.5)
            m=pg.locateOnScreen(r"files\rata.png", confidence=.7)
            pg.moveTo(m)
            pg.click()

    elif ("next" in text):
        time.sleep(1)
        pg.press('pagedown')
        usm.temp += 1
        usm.temp1 += 1
        if (usm.temp == usm.temp1 or (usm.reels_count == usm.temp)):
            usm.reels_count += 1

    elif ("previous" in text):
        time.sleep(1)
        pg.press('pageup')
        usm.temp -= 1

    elif ("reel" in text):
        None

    else:
        find = 0
        return
