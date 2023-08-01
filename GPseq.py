from random import randint


def GP(a, ration, n):
    for i in range(0, n):
        term = a * pow(ration, i)
        print(term, end=" ")
    print(". . . Nth")


GP(randint(1, 10), randint(1, 10), randint(5, 20))