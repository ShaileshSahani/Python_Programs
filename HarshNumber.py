def check_harshad(number, s=0):
    if number == 0:
        return s
    else:
        s += int(number % 10)
        number //= 10
        return check_harshad(number, s)
class HarShadNumber:
    try:
        inp = int(input("Enter a number: "))
        print("Harshad number" if inp % check_harshad(inp) == 0 else "Not Harshad Number")
    except ValueError:
        print("NAN")
