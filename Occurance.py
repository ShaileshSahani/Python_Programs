l = list(map(int, input("Enter the number :").split(" ")))
duplicate = list(set(l))
print("\nDuplicate elements in list :", end=" ")
for i in range(len(duplicate)):
    count = 0
    for j in range(len(l)):
        if duplicate[i] == l[j]:
            count += 1
    if count > 1:
        print(duplicate[i], end=' ')
