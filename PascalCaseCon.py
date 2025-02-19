class Pascal:
    @staticmethod
    def convert(string):
        string = string.capitalize()
        new_str = ''
        for i in range(len(string)):
            if string[i] == " ":
                new_str += " " + string[i + 1].upper()
                i += 1
            else:
                new_str += string[i]
        return new_str

    @staticmethod
    def m2(string):
        lis = []
        for i in string:
            lis.append(i)
        lis[0] = lis[0].upper()
        for i in range(len(lis) - 1):
            if lis[i] == " ":
                lis[i + 1] = lis[i + 1].upper()
                i += 1
        return "".join(lis)


x = input("Enter a string: ")
print(f"Your string: {x}")
print(f"Pascal string: {Pascal.convert(x)}")
print(f"Pascal string: {Pascal.m2(x)}")
