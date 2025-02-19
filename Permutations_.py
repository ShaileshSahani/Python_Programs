from itertools import permutations, combinations, combinations_with_replacement


class PERMUTATIONS:
    @staticmethod
    def all_permutations(list_):
        values = permutations(list_)
        print("All possible Permutations")
        for i in values:
            print(i)

    @staticmethod
    def all_combinations(list_, seq):
        if len(list_) < seq:
            print("No combinations")
        else:
            print("\nAll possible combinations")
            com = combinations(list_, seq)
            for i in com:
                print(i)

    @staticmethod
    def all_combinations_with_replace(list_, seq):
        if len(list_) < seq:
            print("No combinations_with_replacements")
        else:
            print("\nAll possible combinations_with_replacements")
            com = combinations_with_replacement(list_, seq)
            for i in com:
                print(i)


values_ = list(map(int, input("Enter numbers: ").split()))
no_ = int(input("Number of Pairs: "))
PERMUTATIONS.all_permutations(values_)
PERMUTATIONS.all_combinations(values_, no_)
PERMUTATIONS.all_combinations_with_replace(values_, no_)
