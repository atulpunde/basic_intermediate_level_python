##import trymodule
from trymodule import addin

class demo(object):
    def __init__(self,a):
        self.a=a
    def __repr__(self):
        return ("This is from repr = %s"%(self.a))
    def __str__(self):
        return ("This is from str = %s"%(self.a))

class childdemo:
    def __init__(self,b):
        self.b=b
    def prints(self):
        print("This is child demo")
        
d1 = demo(15)
d2 = demo(11)
print(d1)
print(d2)

print("This is main file")

print("Addition of two numbers = ",addin(10,22))

print("__________________________________________")

try:
    fout = open("demod1.txt","r")
    fout.close()    
except FileNotFoundError as fnf:
    print("in except ")
finally:
    print("this is final")
print("rest code")
