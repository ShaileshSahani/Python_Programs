dic = {
    "python 2": 3.8, "python 1": 3.1, "python 3": 3.11
}
for key, values in sorted(dic.items()):
    print(key, values)

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {6: 60, 5: 50}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)

print(sum(dic1.values()))