from time import *
from threading import Thread
def mybox():
   while True:
        print('box is open')
        sleep(5)
        print('box is close')
        sleep(5)
def myled():
    while True:
        print('led is on')
        sleep(1)
        print('led is off')
        sleep(1)
boxThread  = Thread(target=mybox)
ledThread = Thread(target=myled)
boxThread.daemon = True
ledThread.daemon = True
boxThread.start()
ledThread.start()
while True:
    pass

print('this is simple example of threading everyone can understand it easily')