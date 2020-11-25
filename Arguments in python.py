

#types of actual args:
    #1:positional
    #2:default
    #3:keyword
    #4:default

'''__________Required argument__________'''
def sums(a,b,c):    #formal args
    print("Sum is = ",a+b+c)
sums(3,4,5)         #actual args


'''__________Keyword arguments___________'''
def disp(name,age=22):
    print(f"In disp Name = {name} and Age = {age}")
disp(age=23,name="Ajit")


'''__________default arguments___________'''
def student(name,age=24):
    print(f"In student Name = {name} and Age = {age}")
student("Ajit")


'''__________Variable argument____________'''
def fun1(*mylist):
    print("Numbers :")
    print(*mylist)
##    for i in mylist:
##        print(i,end=' ')
    print()
fun1(20,39)
fun1(20,39,34)



