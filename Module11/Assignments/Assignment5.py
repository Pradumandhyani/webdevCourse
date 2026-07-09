# Program to print all substrings of a string

string = input("Enter a string: ")

print("All Substrings are:")

for i in range(len(string)):
    for j in range(i + 1, len(string) + 1):
        print(string[i:j])