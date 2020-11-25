a = 2

def disp():
    a = 4
    a = a+1
    print(a)

    def inner_disp():
        nonlocal a
        a = 3+a
        print(a)
    inner_disp()
    
disp()
print(a)
