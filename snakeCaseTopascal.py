snake_string = input("Enter a string: ")
pascal_str = ""
for i in snake_string:
    if i == " ":
        pascal_str += "_"
    else:
        pascal_str += i
print(pascal_str)

x = "i a a n"
y = x.replace(" ", "_")
print(y)
