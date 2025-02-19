class PrimeFactor:
    @classmethod
    def prime_factor(cls, num):
        values = []
        while num % 2 == 0:
            values.append(2)
            num //= 2
        for i in range(3, int(num ** 1/2), 2):
            while num % i == 0:
                values.append(i)
                num /= i
        if num > 2:
            values.append(num)
        return values


number = int(input("Enter a number: "))
value = PrimeFactor.prime_factor(number)
print("Prime Factors:", value)
