file = open("D://Sem 4//Python//Program Files//BirthDate.txt","w")
file.write("Added")
file.close()

file = open("D://Sem 4//Python//Program Files//BirthDate.txt","r")
for i in file:
    print(i)
file.close()