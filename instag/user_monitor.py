import pygetwindow as gw
import time
import datetime
import pandas as pd
import page_finder as pf
import threading
import voice_to_action as va

open = 0
open1 = 0
run = 1
page = "null"
page2 = "null"
temp = "null"
msg_time = 0.0
reels_time = 0.0
reels_count = 0
temp = 0
temp1 = 0

def check():
    global run
    global open
    global open1
    global page
    global temp
    global msg_time
    global reels_time
    start_time = 0
    global reels_count

    while run == 1:
        windows_list = gw.getAllTitles()
        for i in windows_list:
            if ('Instagram' in i):
                open = 1
                open1 = 1
                break
     
        if (open == 1):
            start_time = time.time()
            break 
    thread_start = 0  
    while run == 1:
        windows_list = gw.getAllTitles()
        for i in windows_list:
            if ('Instagram' in i):
                open = 1
                break
            else:
                open = 0

        if (open == 0):
            break
         
        time.sleep(3)
        if (thread_start == 0):
            thread_start = 1
            thread = threading.Thread(target=page_timer)
            thread.start()

    if ((open == 1 and run == 0) or (open == 0 and open1 != 0)):
        end_time = time.time()
        if (start_time != 0):
            usage_time = end_time - start_time
            r = usage_time/60
            update_data ([round(r,1), round(msg_time,1), round(reels_time,1), reels_count])
        
        else:
            update_data ([0,0,0,0]) 

    else:
        update_data ([0,0,0,0])

def new_day(df,tdate):
    df1 = df
    new = pd.DataFrame({'date':tdate, 'usage_time':[0.0], 'times_opened':[0], 'message_time':[0.0], 'reels_time':[0.0], 'reels_count':[0]})
    df = pd.concat([df1,new])
    return df

def update_data(data):
    ust = data[0]
    mt = data[1]
    rt = data[2]
    rc = data[3]
    if (ust == 0):
        return
    df = pd.read_csv('usm_data.csv')
    tdate = datetime.date.today().strftime("%d-%m-%Y")
    indate = df['date'].iloc[-1]
    if (indate != tdate):
        df = new_day(df,tdate)
            
    df.loc[df.index[-1], 'usage_time'] += ust
    df.loc[df.index[-1], 'times_opened'] += 1
    df.loc[df.index[-1], 'message_time'] += mt
    df.loc[df.index[-1], 'reels_time'] += rt
    df.loc[df.index[-1], 'reels_count'] += rc
    try: 
        df.to_csv('usm_data.csv', index = False)
    except PermissionError:
        print("can't update data. Please close the source file" )
    
    if run == 1:
        check()

def page_timer():
    global msg_time
    global reels_time
    global open
    global run
    global page2
    while (open == 1 and run ==1):
        page = pf.cp()
        st = time.time()
        while (open == 1 and run ==1):
            page2 = pf.cp() 
            if (page == page2):
                continue
            break
        et = time.time()
        pt = et - st
        if (page == 0):
            continue
        elif ("message" in page):
            msg_time += pt
            msg_time = msg_time/60
        elif ("reel" in page):
            reels_time += pt
            reels_time = reels_time/60


def timer(min):
    num = ""
    for i in min:
        if i.isdigit():
            num = num+i
    min = int(num)*60
    for i in range(int(min/2)):
        time.sleep(2)
        if (va.timer != 1):
            return

    window_title = 'Instagram'
    try:
        window= gw.getWindowsWithTitle(window_title)[0]
        window.close()
        time.sleep(1)
    except IndexError:
        return


   
