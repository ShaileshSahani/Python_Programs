number = int(input("Enter a number: "))


def factorial(x):
    if x == 0:
        return 1
    elif x == 1:
        return x

    else:
        return x * factorial(x - 1)


sum_ = 0
temp = number
while number > 0:
    sum_ += factorial(int(number % 10))
    number //= 10
if sum_ == temp:
    print("The number is a KrishnaMurthy number")
else:
    print("Not a KrishnaMurthy number!")
