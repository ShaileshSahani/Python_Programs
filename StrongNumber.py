class StrongNumber:
    @classmethod
    def fact(cls, num):
        if num == 1:
            return num
        else:
            return num * StrongNumber.fact(num - 1)

    @classmethod
    def strong_number(cls, n):
        tem = n
        sum_ = 0
        while n > 0:
            sum_ += StrongNumber.fact(int(n % 10))
            n //= 10
        print("Strong Number" if tem == sum_ else "Not A Strong number")


number = int(input("Enter a number: "))
StrongNumber.strong_number(number)
