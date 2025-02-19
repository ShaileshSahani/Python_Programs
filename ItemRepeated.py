list_values = list(map(int, input("Enter element with single space between: ").split()))
duplicate_removed = list(set(list_values))
print("Repeated values: ", end="")
for i in range(len(duplicate_removed)):
    count = 0
    for j in range(len(list_values)):
        if duplicate_removed[i] == list_values[j]:
            count += 1
    if count > 1:
        print(duplicate_removed[i], end=" ")

