# Program to find the first set bit

num = int(input("Enter a number: "))

if num == 0:
    print("No set bit found.")
else:
    position = 1
    while (num & 1) == 0:
        num = num >> 1
        position += 1
    print("First set bit is at position:", position)