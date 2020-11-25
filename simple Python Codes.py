##n = int(input("Enter Number of input = "))
##L = []
##
##for i in range(n):
##    L.append(input("Enter String = "))
##    
##print("\nGiven List is = ",L)
##
##longStr = maxlambda L:len(L)
##
##print(longStr(L))

##def fun(n):
##    return lambda a,n: a*n
##
##d = fun(2)
##
##print(d(11))

f = lambda x:3*x+1
print(f(2))

fname = lambda fn,ln:fn.strip().title()+" "+ln.strip().title()
print(fname("  AtUl","PunDe"))

mylist = ["abb","mmm","vvv","www","Aaa","ddd","bbb","dff","eee"]
print(mylist)

mylist.sort()
print("Given List is= {}".format(mylist))

cap = map(lambda x:x.upper(),mylist)
print(list(cap))

at = [23,43,12,25,14,45,32,24]
print("sorted = ",sorted(at,reverse=True))
at.sort()

grt = filter((lambda x:x>=20),at)
print(list(grt))

print("sts")





















