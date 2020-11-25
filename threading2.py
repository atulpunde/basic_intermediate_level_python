
#how to create thread in python
#1) without creating class
#2) by extending thread calss
#3) without creating thread class 

##import threading
from threading import *

class mythread(Thread):
    def run(self):
        for i in range(5):
            print("its run ",i)
a = mythread()
a.start()

b = mythread()
b.start()


# a.join()    #join to method so that it is not inttrupted by main method

# print("by from ",current_thread().getName())
