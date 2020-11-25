import re
n = input("Enyter Number = ")

if re.search("*",n):
    print("Correct..")
else:
    print("no")
