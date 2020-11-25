# from date import *
from datetime import date

d = int(input("day = "))
m = int(input("month = "))
y = int(input("year = "))
print(date.today())

dd = date(2020,12,20)
print(dd)

print(date(y,m,d))