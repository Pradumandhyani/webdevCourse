class Expression:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Division by zero is not possible."

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

obj = Expression(num1, num2)

print("Addition:", obj.add())
print("Subtraction:", obj.subtract())
print("Multiplication:", obj.multiply())
print("Division:", obj.divide())