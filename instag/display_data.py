import pandas as pd
import pygetwindow as gw
import matplotlib.pyplot as plt
import datetime
import threading
import time

data = pd.read_csv('usm_data.csv')
data[data.columns[1:]] = data.iloc[:,1:].astype(int)

def maxi():
    time.sleep(2.5)
    window= gw.getWindowsWithTitle('Figure 1')[0]
    window.maximize()

def dashboard():
    t1 = threading.Thread(target=maxi)
    t1.start()
    global data
    df = data
    tdate = datetime.date.today().strftime("%d-%m-%Y")
    indate = df['date'].iloc[-1]
    if (indate != tdate):
        print("No Data Found")
        return
    Messages = df['message_time'].iloc[-1]
    Reels = df['reels_time'].iloc[-1]
    others = df['usage_time'].iloc[-1] - (df['message_time'].iloc[-1] + df['reels_time'].iloc[-1])
    labels = ['Messages', 'Reels','Others']
    values = [Messages, Reels, others]
    plt.pie(values, labels=labels, autopct=lambda p: '{:.0f}'.format(p * sum(values) / 100) + "\n mins")
    plt.title("DASHBOARD\n")
    plt.show()
    
def reels_count():
    t1 = threading.Thread(target=maxi)
    t1.start()
    global data
    df = data
    df = df.tail(7)
    date = df['date']
    reels_count = df['reels_count']
    plt.figure(figsize=(10, 6))
    plt.bar(date, reels_count, color = 'y')
    plt.title('REELS_COUNT')
    plt.grid(axis='y', linestyle='-', color='r', alpha=.6)
    plt.show()

def usage_time():
    t1 = threading.Thread(target=maxi)
    t1.start()    
    global data
    df = data
    df = df.tail(7)
    date = df['date']
    usage_time = df['usage_time']/60
    plt.figure(figsize=(10, 6))
    plt.bar(date, usage_time, color = 'y')
    plt.title('USAGE_TIME')
    plt.grid(axis='y', linestyle='-', color='r', alpha=.6)
    plt.show()
    