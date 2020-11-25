import time

print("\nDisplay Time..\n")
locTime = time.asctime(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))

print("\nSquares")
arr = [1,2,3,4,5]
for sq in arr:
    print(sq*sq,end = " ")

print("\nSerial Numbers")
for i in range(0,11):
    print(i,end=" ")

print("\nPrint Pattern")
n = 4
for i in range(n):
    for i in range(i+1):
        print("*",end=" ")
    print()

print("\U0001F602")
print("\U0001F604")
print("\U0001F606")
print("\U0001F608")

