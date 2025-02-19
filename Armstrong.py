class Armstrong:
    @classmethod
    def armstrong_(cls, number):
        total = 0
        temporary = number
        while number > 0:
            remainder = int(number % 10)
            total += remainder ** 3
            number //= 10
        if total == temporary:
            return True


obj = Armstrong()
try:
    number_ = int(input("Enter number of test: "))
    value = obj.armstrong_(number_)
    if value is True:
        print("The number is armstrong")
    else:
        print("Not an armstrong")
except ValueError:
    print("Not An Integer")
