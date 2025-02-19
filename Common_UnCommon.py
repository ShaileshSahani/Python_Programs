factor1 = [2, 2, 2, 3, 3, 11]
factor2 = [2, 2, 2, 2, 3, 3, 5, 5]
intersection = []
for i__ in factor1:
    if i__ in factor2:
        intersection.append(i__)
        factor2.remove(i__)
for i__ in intersection:
    factor1.remove(i__)
print(factor1)
print(factor2)
print(intersection)


