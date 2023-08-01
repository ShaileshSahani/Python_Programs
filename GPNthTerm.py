def Find(a, ratio, term):
    nth = a * (ratio ** (term - 1))
    print(f"The {term}th term of GP is: {nth}")


list_ = list(map(int, input("Enter The Numbers with One Space: ").split()))
lis1 = []
for i in range(len(list_) - 1):
    lis1.append(int(list_[i + 1] / list_[i]))
lis1 = list(set(lis1))
if len(lis1) == 1:
    for i in list_:
        print(i, end=" ")
    print(". . . nth")
    x = int(input("Enter The Term You Want To Find: "))
    Find(list_[0], lis1[0], x)
else:
    print("No GP exists")