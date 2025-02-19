from random import randint


class LowestCommonMultiple:

    @classmethod
    def prime_factor(cls, num):
        values = []
        while num % 2 == 0:
            values.append(2)
            num //= 2
        for i_f in range(3, int(num ** 1 / 2), 2):
            while num % i_f == 0:
                values.append(i_f)
                num /= i_f
        if num > 2:
            values.append(num)
        return values

    @classmethod
    def find_lcm(cls, number1, number2):
        factor1 = LowestCommonMultiple.prime_factor(number1)
        factor2 = LowestCommonMultiple.prime_factor(number2)
        print(f"Prime Factors of {number1}: ", end=" ")
        for s in factor1:
            print(s, end=" ")
        print(f"\nPrime Factors of {number2}: ", end=" ")
        for s in factor2:
            print(s, end=" ")
        intersection = []
        for i__ in factor1:
            if i__ in factor2:
                intersection.append(i__)
                factor2.remove(i__)
        for i__ in intersection:
            factor1.remove(i__)
        lcm = 1
        for a in factor1 + factor2 + intersection:
            lcm *= a
        print(f"\nLowest Common multiple of {number1}, {number2} = {lcm}\n")


for i in range(10):
    LowestCommonMultiple.find_lcm(randint(2, 100), randint(2, 100))
