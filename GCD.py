class GreatestCommonD:
    @classmethod
    def gcd_(cls, num1, num2):
        number = 1
        for i in range(1, min(num1, num2) + 1):
            if num1 % i == 0 and num2 % i == 0:
                number = i
        return number


number1 = int(input("Enter a number: "))
number2 = int(input("Enter a number: "))
print(GreatestCommonD.gcd_(number1, number2))
