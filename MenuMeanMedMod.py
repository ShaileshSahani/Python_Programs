def mean(lis):
    men = sum(lis) / len(lis)
    print(f"\nMean of the Values is: {men}\n")


def median(lis):
    lis.sort(reverse=False)
    val = len(lis) // 2
    if val % 2 == 1:
        print(lis[val])
    else:
        val1 = (lis[val - 1] + lis[val]) / 2
        print(round(lis[val], 2))


def mode(lis):
    lis1 = []
    for i in range(len(lis)):
        for j in range(i + 1, len(lis)):
            if lis[i] == lis[j]:
                lis1.append(lis[j])
                break
            else:
                continue
    lis1 = set(lis1)
    lis1 = list(lis1)
    if len(lis1) == 0:
        print("No Mode Exist")
    elif len(lis1) == 1:
        print("Mode: ", lis1[0])
    elif len(lis1) == 2:
        print("Bimodal: ", lis1[0], lis1[1])
    elif len(lis1) == 3:
        print("Bimodal: ", lis1[0], lis1[1], lis1[2])
    else:
        print("MultiModal: ", lis1)


values = list(map(int, input("Enter Values of list: ").split()))
print(values)
while True:
    user = int(input("\n1.Mean\t2.Median\t3.Mode\t4.Exit\nEnter Your Choice: "))
    if user == 1:
        mean(values)
    elif user == 2:
        median(values)
    elif user == 3:
        mode(values)
    elif user == 4:
        print("\nYou Exit\n")
        break
    else:
        print("\nInvalid Input\n")
