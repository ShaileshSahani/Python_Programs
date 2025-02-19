r = int(input('enter row elements:'))
c = int(input('enter column elements:'))
matrix = []
for i in range(r):
    a = []
    for j in range(c):
        k = int(input('enter'))
        a.append(k)
    matrix.append(a)
for i in range(r):
    for j in range(c):
        print(matrix[i][j], end=" ")
    print()
