x = lambda num: 1 if num <= 1 else num*x(num - 1)
print(x(5))