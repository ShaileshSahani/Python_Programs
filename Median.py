# find median
lis = list(map(int, input("Enter Numbers: ").split()))
lis.sort(reverse=False)
print(lis)
val = len(lis) // 2
print(val)
if val % 2 == 1:
    print(lis[val])
else:
    val1 = (lis[val - 1] + lis[val]) / 2
    print(round(lis[val], 2))
