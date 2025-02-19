x = [1, 3, 5, 8, 5, 3, 5, 1, 2, 3]
n = len(x) // 2
s = x[:n:] + x[len(x):n - 1:-1]
for i in s:
    print(i, end=" ")
