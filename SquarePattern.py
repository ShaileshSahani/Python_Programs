n = int(input('Enter the number of rows='))
for i in range(n):
    for j in range(n):
        if (i == 0 or i == n / 4 or i == n - 1 or i == n / 2 or
                j == 0 or j == n / 4 or j == n - 1 or j == n / 2 or
                i == n or i == n / 2 + n / 4 or j == n / 2 + n / 4):
            print('*', end=' ')
        else:
            print(end='  ')
    print()
