class AutoMorphic:
    def __init__(self, number):
        self.number = number

    # M1
    def by_slice(self):
        value = int(str(self.number ** 2)[-len(str(self.number))::])
        if value == self.number:
            return True
        else:
            return False

    # M2
    def by_modulus(self):
        mod = pow(10, len(str(self.number)))
        if (self.number ** 2) % mod == self.number:
            return True
        else:
            return False

    # M3
    def by_string(self):
        s = self.number
        if str(s ** 2).endswith(str(s)):
            return True
        else:
            return False

    # M4
    def by_loop(self):
        while self.number > 0:
            sq = self.number ** 2
            if self.number % 10 == sq % 10:
                self.number //= 10
                sq //= 10
                return True
            else:
                return False


# For Single
val = int(input("Enter a number: "))
ob = AutoMorphic(val)
if ob.by_modulus() and ob.by_loop():
    print("Auto Morphic Number")
else:
    print("Not")

# for a range
print("\nBetween 0 to 100000")
for i in range(100000):
    obj = AutoMorphic(i)
    if obj.by_string():
        print(i, " Auto Morphic Number")
    else:
        continue
