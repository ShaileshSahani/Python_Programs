x = list(map(int, input("Enter Numbers one space Between: ").split()))
n = sorted(set(x))
for i in range(len(n)):
    count = 0
    for j in range(len(x)):
        if n[i] == x[j]:
            count += 1
    print(f"Element {n[i]} present {count} times")