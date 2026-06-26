print("===== Robot Introduction =====")

robot_name = input("Enter Robot Name: ")
robot_version = input("Enter Robot Version: ")
user_name = input("Enter Your Name: ")
age = int(input("Enter Your Age: "))

print("\n----- Introduction -----")
print("Hello,", user_name + "!")
print("My name is", robot_name + ".")
print("I am version", robot_version + ".")
print("I am designed to help people with different tasks.")

if age < 18:
    print("You are a student. I can help you with your studies.")
else:
    print("I can assist you with work, learning, and daily activities.")

print("Nice to meet you!")
print("Have a great day!")