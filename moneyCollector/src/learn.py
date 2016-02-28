import pprint, pickle
import pyHook
import pythoncom

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
    gClicks.add(event.Position)
    return True

#install mouse callback
hm = pyHook.HookManager()
hm.SubscribeMouseAllButtonsDown(onclick)
hm.HookMouse()
pythoncom.PumpMessages()

while True:
    choice = raw_input("> ")

    if choice == 's' :
        print "Quiting..."
        break

hm.UnhookMouse()
saveData(gClicks)
