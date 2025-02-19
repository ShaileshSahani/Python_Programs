class NumCheck:
    def __init__(self, number):
        self.number = number

    def check_number(self):
        if self.number > 0:
            print("Positive")
        elif self.number < 0:
            print("Negative")
        else:
            print("Its Zero")


try:
    num = int(input("Enter a number: "))
    ob = NumCheck(num)
    ob.check_number()
except ValueError:
    print("Value No suitable(NAN)")
