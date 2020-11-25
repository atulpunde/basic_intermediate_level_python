# Atul Rajaram Punde
# Roll No 1655

# Q4.   Write a python program to create a thread and perform 
# read and write operations on file using these threads.

from threading import *

class FileOperation(object):
    def Write(self):
        for i in range(5):
            print(i*3)

    def Read(self):
        for i in range(5):
            print(i*2)

if __name__ == "__main__":
    file = FileOperation()  # Creating object of class 

    thread1 = Thread(target=file.Write())   
    thread2 = Thread(target=file.Read())    

    thread1.start() # Starting both thread
    thread2.start()
    