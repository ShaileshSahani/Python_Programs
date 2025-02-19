class ProNic:
    @staticmethod
    def pro_nic_number(number):
        for i in range(1, number // 2):
            if i * (i + 1) == number:
                return True
        return False


try:
    num = int(input("Enter a number: "))
    state = ProNic.pro_nic_number(num)
    print("ProNic Number" if state else "Not")
except ValueError:
    print("NaN")
