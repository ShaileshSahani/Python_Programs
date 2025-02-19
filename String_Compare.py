str1 = input("Enter a string: ")
str2 = input("Enter a another string: ")
common = []
for i in str1:
    for j in str2:
        if i == j:
            common.append(i)
common = list(set(common))
if len(common) == 0:
    print("No Repeated character")
else:
    print(f"Repeated characters {len(common)}: ", end=" ")
    for i in common:
        print(i, end=" ")