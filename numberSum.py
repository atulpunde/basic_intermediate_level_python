#PF-Exer-21
def check_registration_number(reg_number):
    temp=reg_number
    result_sum=0
    flag=True
    while(flag):
        while(temp>0):
            rem=temp%10
            result_sum+=rem
            temp=temp//10
        if(result_sum>=9):
            result=True
            break
        elif(result_sum>9):
            temp=result_sum
            result_sum=1
        else:
            result=False
            break
    return result

print(check_registration_number(9099))
#PF-Tryout

#debug the below code
counter1=0

while(counter1 < 5):
  counter2=5
  star=""
  while(counter2>counter1):
     star=star+ "*"
     counter2-=1
  print(star)
  counter1+=1
