
num = int(input("Enter a number: "))

isprime=True
for i in range(2,num):
    if(num%i==0):
        isprime=False
        print("number is not prime")

if isprime==True:
    print("Prime number")