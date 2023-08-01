def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


a1 = int(input("Enter first number:"))
b1 = int(input("Enter second number:"))
GCD = gcd(a1, b1)
print("GCD is: ")
print(GCD)

num1, num2 = map(int, (list(input("Enter Numbers Comma separated: ").split())))
gcd = 1
for i in range(1, min(num1, num2)):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i
print(f"GCD of {num1}, {num2} is {gcd}")
