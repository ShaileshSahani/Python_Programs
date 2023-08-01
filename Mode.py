lis = list(map(int, input("Enter Element Of List: ").split()))
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
