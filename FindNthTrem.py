try:
    num = list(map(int, input("Enter AP series: ").split(",")))
    for i in num:
        print(i, end=" ")
    print("....nth")
    lis = []
    for i in range(len(num) - 1):
        lis.append(num[i + 1] - num[i])
    lis = list(set(lis))
    if len(lis) > 1:
        print("\nThe Sequence You Entered is not an AP!")
    else:
        find = int(input("Enter the term Number: "))
        term = (num[0] + (find - 1) * lis[0])
        print(f"{find}th Term Of the AP is {term}")
except Exception as Er:
    print("Error: ", Er)
