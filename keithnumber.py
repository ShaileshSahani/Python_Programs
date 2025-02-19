class Keith:
    @staticmethod
    def check_keith(number):
        sequence = [int(digit) for digit in str(number)]
        size = len(sequence)
        sq = sequence.copy()
        while True:
            next_term = sum(sq[-size:])
            if next_term == number:
                return True
            elif next_term > number:
                return False
            sq.append(next_term)
if Keith.check_keith(197):
    print("Keith Number")
else:
    print("Not")
