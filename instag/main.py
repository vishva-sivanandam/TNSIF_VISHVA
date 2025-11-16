import voice_to_action as va
import voice_assistant as vs
import user_monitor as usm
import speedtest
import threading
import pyautogui as pg

pg.FAILSAFE = False

def check():
    try:
        st = speedtest.Speedtest()
    except speedtest.ConfigRetrievalError:
        print("No Internet Connection!")
        return
    print("Testing Internet Speed...")
    download_speed = st.download() / 1_000_000
    ds = round(download_speed/8,2)
    print ("Your Internet Connection Speed","->",ds,"Mbs")
    if (ds <1 ):
        print("Please Try Again Later")
        return
    elif (ds < 2):
        print("You Have Poor Internet Connection. It May Affect The System's  Performance")
        print("PRESS\n1.exit\n2.Continue Anyway")
        ch = input()
        if (ch == "1"):
            print("Exiting...")
            return
        elif (ch == "2"):
            main()
    else:
        main()
    return

def main():
    thread1 = threading.Thread(target=usm.check)
    thread1.start()

    while 1 :
        text = vs.speech_to_text()
        if (text == 0):
            pass
        elif (text == 1):
            break
        elif("exit" in text):
            usm.run = 0
            vs.text_to_speech("exiting")
            exit()
        else:
            va.check(text)
            pg.moveTo(0,0)

main()

