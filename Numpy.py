import numpy as np
n = []
for i in range(1, 10):
    n.append(i)
s = np.array(n)
print(s.shape)
n1 = s.reshape(3, 3)
print(n1)
