import time as t


def armstrong(n):
    s = 0
    tem = n
    while n:
        rem = int(n % 10)
        s = s + (rem * rem * rem)
        n = n // 10
    try:
        if s == tem:
            print("Test Passed")
            print("Its  An Armstrong Number\n")
        else:
            print("Armstrong Test Failed\n")
    except Exception as e:
        print("An Internal Error!!", e)


def palin(n):
    s = 0
    tem = n
    while n != 0:
        rem = int(n % 10)
        s = (s * 10) + rem
        n = n // 10
    try:
        if tem == s:
            print("Test Pass")
            print("The Number Is a Palindrome\n")
        else:
            print("Palindrome Test Failed\n")
    except Exception as e:
        print("An Internal Error!!", e)


def get_fact(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


def strong(n):
    try:
        s = 0
        tem = n
        while n:
            rem = int(n % 10)
            s = s + get_fact(rem)
            n = int(n / 10)
        if tem == s:
            print("Strong Test Passed")
            print("Its A Strong Number\n")
        else:
            print("Strong Test Failed\n")
    except Exception as e:
        print("An Internal Error!!", e)


def reverse(n):
    s = 0
    while n:
        rem = int(n % 10)
        s = (s * 10) + rem
        n = int(n / 10)
    try:
        print("Reverse Test Pass")
        print("Reversed:", s, "\n")
    except Exception as e:
        print("An Internal Error!!", e)


def sum_of(n):
    s1 = 0
    while n:
        rem = int(n % 10)
        s1 = s1 + rem
        n = n // 10
    print('Sum Of Digits:', s1, "\n")


def count_of(n):
    count = 0
    while n:
        int(n % 10)
        count = count + 1
        n = n // 10
    print("Count Of digits:", count, "\n")


x = int(input("Enter Number:"))
t.sleep(2)
armstrong(x)
t.sleep(2)
palin(x)
t.sleep(2)
strong(x)
t.sleep(2)
reverse(x)
t.sleep(2)
sum_of(x)
t.sleep(2)
count_of(x)
