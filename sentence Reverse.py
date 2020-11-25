s = "Fc Clg Pune "
for i in s[::-1]:
##    print(i,end="")
    if i==" ":
        k = s.index(" ")
        k=k+1
        while True:
            if s[k]==" ":
                continue
            else:
                print(s[k])
            k=k+1
        
