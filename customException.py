class VoteError(Exception):
    def VoteError(self,e):
        super().__init__(e)

class LessThanZeroError(Exception):
    def __init__(self,e):
        self.e = e
        

try:
    age = int(input("Enter age = "))
    
    if age>18:
        raise VoteError("Your age is valid.")
    elif age<0:
        raise LessThanZeroError("Negative Input ")
    else:
        print("Valid input")
        
except VoteError as e:
    print(e,age)
except LessThanZeroError as z:
    print(z,age)
else:
    print("No exceptions..")
finally:
    print("Program Terminaed..")
