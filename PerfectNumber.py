class PerfectNumber:
    @staticmethod
    def perfect_num(num):
        find = 0
        for i in range(1, num//2+1):
            if int(num % i) == 0:
                find += i
        print(f"{num} is Perfect" if num == find else f"{num} is not Perfect")


try:
    number = int(input("Enter a number: "))
    PerfectNumber.perfect_num(number)
except ValueError:
    print("NaN")
