##import threading

from threading import *

child = Thread()
child.start()
print(current_thread().getName())
print("Done")
