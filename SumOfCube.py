from time import time
number = int(input("Enter a number: "))
st = time()
result = 0
for i in range(number + 1):
    result += i ** 3
print(f"Sum of Cube {number} is {result}")
print(time() - st)