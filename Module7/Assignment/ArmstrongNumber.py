# Armstrong Number Program

num = int(input("Enter a number: "))

# Store original number
original_num = num

# Count number of digits
digits = len(str(num))

# Calculate sum of digits raised to power
sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit ** digits
    num = num // 10

# Check Armstrong number
if sum == original_num:
    print(original_num, "is an Armstrong number")
else:
    print(original_num, "is not an Armstrong number")