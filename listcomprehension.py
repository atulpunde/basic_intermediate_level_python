##[ (a,b) for a in range(3) ]
##d = {}

##a = "abcdefghijklmn"
b = [2,3,4,5]
##    
##print(a)
##print(b)
##
##print(list(reversed(a)))
##
##print(sum(b))
####print(b.append([7,8]))
##print(b[::-1])
##print(list(reversed(b)))
##print(max(b))
# Function definition is here
##def printinfo( arg1, *vartuple ):
##   "This prints a variable passed arguments"
##   print ("Output is: ")
##   print ("+",arg1)
##   for var in vartuple:
##      print (var)
##   return;
##
### Now you can call printinfo function
##printinfo( 10,20 )
##printinfo( 70, 60, 50 ,80,90)

##print(b[1:3])
##b[1:2] = []
##print(b)
##print(0xA+0xb)
##print([[i+j for i in "abc"] for j in "def"])
##
##for j in "def":
##    for i in "abc":
##        print(list('i+j'),end="")
##    
##print([if i%2==0: i; else: i+1; for i in range(4)])
##print([1/x for x in (1, 2, 3)])

##ret = list(map(lambda x: x**-1, [1, 2, 3]))
##
##print(ret)

##numberGames = {}
##numberGames[(1,2,4)] = 8
##numberGames[(4,2,1)] = 10
##numberGames[(1,2)] = 12
##sum = 0
##for k in numberGames:
##    print(k)
##    sum += numberGames[k]
##print( len(numberGames) + sum)
##








class someError (Exception):
    def someError(e):
        super(e)
try:
    if '1'!=1:
        raise someError("Some error has Occured")
    else:
        print("some error has not occured")
except someError as e:
    print("In except block: ",e)















