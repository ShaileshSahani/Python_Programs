x = int(input("Binary number:"))
s = 0
i = 0
while x:
    r = int(x) % 10
    s = s + r * pow(2, i)
    x = int(x) / 10
    i += 1
n = s ^ (s >> 1)
s = []
while n:
    s.append(n % 2)
    n = int(n / 2)
print("Gray code:", end='')
for i in s[::-1]:
    print(i, end='')
