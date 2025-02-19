import random

string = input("Enter a number: ")
string_values = "abcdefghijklmnopqrstuvwxyz"
lis = [i for i in string_values]
count = 0
while True:
    match = ""
    for i in range(len(string)):
        match += random.choice(lis)
    count += 1
    if string == match:
        print(f"Found match in {count} iterations")
        break
