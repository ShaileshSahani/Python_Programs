x = list(map(int, input("Enter Numbers one space Between: ").split()))
Min = x[0]
Max = x[0]
print(x)
for i in range(len(x)):
    if Min > x[i]:
        Min = x[i]
    if Max < x[i]:
        Max = x[i]
print(f"The Smallest element is {Min} and Largest element is {Max}")

