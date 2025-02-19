import random


class PrimeFactor:
    @classmethod
    def prime(cls, num):
        lis = []
        for i in range(2, num):
            if num % i == 0:
                lis.append(i)
                num //= i
        print(lis)


for i_ in range(20):
    s = random.randint(1, 50)
    print(s)
    PrimeFactor.prime(s)
