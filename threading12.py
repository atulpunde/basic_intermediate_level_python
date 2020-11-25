
from threading import *

print(current_thread().getName())

def mt():
    print("Child thread")

def mythread():
    print("\nmy thread")

child = Thread(target=mt)
child.start()

myt = Thread(target=mythread)
myt.start()
