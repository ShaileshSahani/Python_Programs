import random


class GrayConversion:
    @staticmethod
    def bin_to_gray(number):
        tem = number
        iterator = 0
        s_ = 0
        while number > 0:
            s_ += (int(number) % 10) << iterator
            number = int(number) / 10
            iterator += 1
        dec_gray = s_ ^ (s_ >> 1)
        gray = []
        while dec_gray > 0:
            gray.append(int(dec_gray) % 2)
            dec_gray = int(dec_gray) // 2
        print(f"\nGrey code for BCD({tem}) = ", end="")
        for i in gray:
            print(i, end="")


for i_m in range(10):
    str1 = ""
    for i_ in range(4):
        str1 += random.choice(["0", "1"])
    GrayConversion.bin_to_gray(int(str1))

