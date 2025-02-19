class PerfectSquare:
    @classmethod
    def perfect_square(cls, num):
        value = int(pow(num, 1/2))
        print(value)
        if value ** 2 == num:
            print("Perfect Square")
        else:
            print("Not")


PerfectSquare.perfect_square(36)
