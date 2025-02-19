class CheckAdditionOfTwoPrime:
    @classmethod
    def check(cls, num):
        values = []
        for i in range(2, num):
            flag = 0
            for j in range(2, i):
                if i % j == 0:
                    flag += 1
                    break
            if flag == 0:
                values.append(i)
        return values

    @classmethod
    def sum_of_prime(cls, val, num):
        flag = 0
        for i in range(len(val)):
            for j in range(i, len(val)):
                if num == val[i] + val[j]:
                    flag += 1
                    print(f"{number} is Addition of Prime Number{val[i], val[j]}")
                    break
        if flag == 0:
            print("No Prime addition Suits")


try:
    number = int(input("Enter a number: "))
    if number == 0 or number < 0:
        print("Not Prime")
    else:
        lis = CheckAdditionOfTwoPrime.check(number)
        CheckAdditionOfTwoPrime.sum_of_prime(lis, number)
except ValueError:
    print("NaN")
