import threading

# tableof = int(input("Table of = "))

class Table(threading.Thread):
    def run(self):
        for i in range(5):
            print(i)

nthread = int(input("Enter Nuber Of Thread = "))

t=[]
for i in range(nthread):
    t1 = Table()
    t.append(t1)

for i in t:
    i.start()
    # i.join()
