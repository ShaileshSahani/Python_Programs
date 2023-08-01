def Solve(a, common, nth):
    sum1 = (int(nth / 2) * (2 * a + (nth - 1) * common))
    return sum1


lis = list(map(int, input("Enter Your Number Separated by single-space: ").split()))
value = []
print(lis)
for i in range(len(lis) - 1):
    value.append(lis[i + 1] - lis[i])
value = list(set(value))

if len(value) == 1:
    x = int(input("Enter The Last Term To Find Sum: "))
    s = Solve(lis[0], value[0], x)
    print("The sum of nth term is: ", s)
else:
    print("The Given Sequence is not an AP")