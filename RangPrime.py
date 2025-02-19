class Prime:
    @staticmethod
    def find_prime(rang):
        for i in range(2, rang):
            count = 0
            for j in range(2, i):
                if i % j == 0:
                    count += 1
                    break
            if count == 0:
                print(i, end=" ")

print("Prime Number in range(1, 50)")
Prime.find_prime(50)
