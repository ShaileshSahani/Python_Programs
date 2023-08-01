import numpy as np
n = int(input("Enter The Number Of Element You Want To Enter: "))
val_List = []
for i in range(n):
    v = int(input())
    val_List.append(v)
val_arr = np.array([n ** 2 for n in val_List])
print(val_arr)
