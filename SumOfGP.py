def Find(a, ratio, term):
    if ratio > 1:
        sum1 = a * ((ratio ** term - 1) / (ratio - 1))
        print("Sum Of GP: ", sum1)
    elif ratio < 1:
        sum1 = a * ((1 - ratio ** term) / (1 - ratio))
        print("Sum Of GP: ", sum1)
    else:
        print(term)


list_ = list(map(int, input("Enter The Numbers with One Space: ").split()))
lis1 = []
for i in range(len(list_) - 1):
    lis1.append(int(list_[i + 1] / list_[i]))
lis1 = list(set(lis1))
if len(lis1) == 1:
    for i in list_:
        print(i, end=" ")
    print(". . . nth")
    x = int(input("Enter The Term You Want To Find Sum: "))
    Find(list_[0], lis1[0], x)
else:
    print("No GP exists")
