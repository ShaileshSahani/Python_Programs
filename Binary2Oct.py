# TODO
# Step 1:
# Binary To Decimal
def convert_dec(number):
    reverse = number[::-1]
    s = 0
    j = 0
    for i in reverse:
        s += int(i) * (2 ** j)
        j += 1
    return s

# Step 2:
# Decimal To Octal
def to_octal(number):
    octal = []
    while number > 0:
        octal.append(int(number % 8))
        number //= 8
    return octal[::-1]

print(to_octal(convert_dec("10101")))


