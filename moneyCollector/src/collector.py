import pprint, pickle
import win32api, win32con
import datetime, threading
import time

gClicks = []

def saveData(data):
    output = open('data.pkl', 'wb')
    pickle.dump(data, output) # Pickle dictionary using protocol 0.
    output.close()

def loadData():
    pkl_file = open('data.pkl', 'rb')
    data = pickle.load(pkl_file)
    pkl_file.close()
    pprint.pprint(data)
    return data

def click(x,y):
    win32api.SetCursorPos((x,y))
    #win32api.mouse_event(win32con.MOUSEEVENTF_MOVE | win32con.MOUSEEVENTF_ABSOLUTE, \
    #win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, \
    #int(x/SCREEN_WIDTH*65535.0), int(y/SCREEN_HEIGHT*65535.0))

    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

gClicks = loadData()

def collectMoney():
    for d in gClicks:
        click(d[0] ,d[1])
        print d
        time.sleep(1)
    threading.Timer(10, collectMoney).start()

collectMoney()
