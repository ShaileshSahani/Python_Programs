bin_val = input("Enter a binary number: ")


def check_binary(bin_):
    list_ = []
    try:
        for _ in bin_:
            list_.append(int(_))
    except ValueError:
        return list_
    return list_


s = check_binary(bin_val)
if len(s) == 0 or max(s) > 1:
    print("The number you entered isn't a binary number!!")
else:
    bin_val = int(bin_val)
    temp = bin_val
    power = 0
    value = 0
    while bin_val > 0:
        remainder = int(bin_val % 10)
        value += remainder * (2 ** power)
        bin_val //= 10
        power += 1
    print(f"The Decimal number for {temp} is ", value)
    print(f"The Octal number for {temp} is ", end="")
    octal = []
    hex_val = value
    while value > 0:
        octal.append(int(value % 8))
        value //= 8
    for _ in octal[::-1]:
        print(_, end="")

    hexa = ""
    conversion = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9",
                  10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    while hex_val > 0:
        remain = hex_val % 16
        hexa = conversion[remain] + hexa
        hex_val //= 16
    print(f"\nThe Hexa-Decimal number for {temp} is ", hexa)
