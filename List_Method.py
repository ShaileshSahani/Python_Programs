# p1
list1 = [n for n in range(10) if n % 2 == 0]
print(list1)

# p2 m1 normal method for nested list
l1 = []
for i in range(3):
    l1.append([])
    for j in range(5):
        l1[i].append(j)
print(l1)

# p2 m2 nested list I know
li = []
for i in range(3):
    l2 = []
    for j in range(1, 4):
        l2.append(j)
    li.append(l2)
print(li)
for i in range(len(li)):
    for j in range(len(li)):
        print(li[i][j], end=" ")
    print()

# p3 nested list
l3 = [[i for i in range(5)]for j in range(3)]
print(l3)

# p4 square number m1
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new1 = [val ** 2 for val in n]
print(new1)

# p4 square normal m2
n1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s = 1
for i in n:
    s = i ** 2
    print(s, end=" ")
