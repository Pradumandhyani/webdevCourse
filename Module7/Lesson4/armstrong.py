num=int(input("enter the number"))
temp=num
while num>0:
    rem=num%10
    sum= sum+rem*rem*rem
    num=num//10
    

if sum==temp:
    print("armstrong number")
else:
    print("not armstrong")