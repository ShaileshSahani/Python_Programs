num1, den1 = map(int, list(input("Enter Numerator and Denominator of number 1: ").split()))
print(num1, den1)
num2, den2 = map(int, list(input("Enter Numerator and Denominator of number 1: ").split()))
print(num1, den1)
Numerator = num1 * den2 + num2 * den1  # change sign for Subtraction of Fraction
Denominator = den1 * den2


def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)


div = GCD(Numerator, Denominator)
Num = int(Numerator / div)
Dem = int(Denominator / div)
print(f"{num1} / {den1} + {num2} / {den2} = {Num} / {Dem}")
