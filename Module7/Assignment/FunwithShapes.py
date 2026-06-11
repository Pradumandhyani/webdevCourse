# Fun with Shapes Program

print("Fun with Shapes")
print("1. Area of Circle")
print("2. Area of Rectangle")
print("3. Area of Square")
print("4. Area of Triangle")

choice = int(input("Enter your choice: "))

if choice == 1:
    radius = float(input("Enter radius of circle: "))
    area = 3.14 * radius * radius
    print("Area of Circle =", area)

elif choice == 2:
    length = float(input("Enter length of rectangle: "))
    breadth = float(input("Enter breadth of rectangle: "))
    area = length * breadth
    print("Area of Rectangle =", area)

elif choice == 3:
    side = float(input("Enter side of square: "))
    area = side * side
    print("Area of Square =", area)

elif choice == 4:
    base = float(input("Enter base of triangle: "))
    height = float(input("Enter height of triangle: "))
    area = 0.5 * base * height
    print("Area of Triangle =", area)

else:
    print("Invalid choice")