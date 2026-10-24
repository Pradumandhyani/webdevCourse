num=int(input("enter te number "))
isprime=True

for i in range(2,num):
    if(num%i==0):
        print("not a prime number")
        isprime=False
        break

if isprime==True:
    print("Prime number")