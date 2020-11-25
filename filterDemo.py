### list of alphabets
##alphabets = ['a', 'b', 'd', 'e', 'i', 'j', 'o']
##
### function that filters vowels
##def filterVowels(alphabet):
##    vowels = ['a', 'e', 'i', 'o', 'u']
##
##    if(alphabet in vowels):
##        return True
##    else:
##        return False
##
##filteredVowels = filter(filterVowels, alphabets)
##
##print('The filtered vowels are:')
##for vowel in filteredVowels:
##    print(vowel)

##a = "aaa"
##b = str(10.9)
##print(a,type(a))
##print(b)
##print(type(b))

##list1 = [12,234,45,6,7,8,9]
##
##odd = filter(lambda i:i%2==0,list1)
##multi = map(lambda i:i*2,list1)
##print(list(odd))
##print(list(multi))

##list1 = [12,234,45,6,7,8,9]
table = lambda i:i*2

for i in range(11):
    print(table(i))
