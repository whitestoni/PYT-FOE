import pprint, pickle
import pyHook
import pythoncom
import sys
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

def onclick(event):
    global gClicks
    data = event.Position
    print data
    gClicks.append(event.Position)
    return True

def onKeyBoard(event):
    global gClicks
    print event.Key
    if event.Key == 'Q':
        hm.UnhookMouse()
        hm.UnhookKeyboard()
        print 'Exit!!'
        sys.exit(0)
        return False
    elif event.Key == 'R':
        gClicks = []
        print 'Reset Data'
        time.sleep(1)
    elif event.Key == 'S':
        saveData(gClicks)
        print 'Saved!!'
        time.sleep(1)
    return True


#install mouse callback
hm = pyHook.HookManager()
hm.SubscribeMouseAllButtonsDown(onclick)
hm.SubscribeKeyAll(onKeyBoard)
hm.HookMouse()
hm.HookKeyboard()
pythoncom.PumpMessages()
hm.UnhookMouse()
hm.UnHookKeyboard()
