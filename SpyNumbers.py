number = int(input("Enter a number: "))
sum_ = 0
product = 1
while number > 0:
    remainder = int(number % 10)
    sum_ += remainder
    product *= remainder
    number //= 10
if sum_ == product:
    print("The number is a spy number")
else:
    print("No spy number!")
    