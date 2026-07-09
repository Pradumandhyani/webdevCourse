# Program to implement a simple logic circuit
# Output = (A AND B) OR (NOT C)

A = int(input("Enter A (0 or 1): "))
B = int(input("Enter B (0 or 1): "))
C = int(input("Enter C (0 or 1): "))

output = (A and B) or (not C)

print("Output:", int(output))