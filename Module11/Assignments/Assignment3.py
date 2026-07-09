# Program to reverse bits of an 8-bit number

num = int(input("Enter a number: "))

reverse = 0

for i in range(8):
    reverse = (reverse << 1) | (num & 1)
    num = num >> 1

print("Reversed bits (Decimal):", reverse)
print("Reversed bits (Binary):", bin(reverse))