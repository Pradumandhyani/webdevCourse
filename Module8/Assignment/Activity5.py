import math

n = int(input("Enter the number of sides: "))
s = float(input("Enter the length of each side: "))

area = (n * s * s) / (4 * math.tan(math.pi / n))

print("Area of the regular polygon =", round(area, 2))