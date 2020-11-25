
#how to create thread in python
#1) without creating class
#2) by extending thread calss
#3) without creating thread class 

##without creating thread class

from threading import *

class Example:
    def myfun(self):
        for i in range(5):
            print("its run ",i)
            print("by from ",current_thread().getName())
ex = Example()

t1 = Thread(target=ex.myfun)

t1.start()
t1.join()   #join to method so that it is not inttrupted by main method

print("by from ",current_thread().getName())
print("Done")



##thread class method
##thread synchronization