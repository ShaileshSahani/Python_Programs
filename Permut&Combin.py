def fact(n):
    if n > 0:
        return n * fact(n - 1)
    else:
        return 1


n = int(input("Enter The Number of Object: "))
r = int(input("Enter The Combinations for each pair: "))
if n < r:
    print("Item Out of Range")
else:
    Permutation = fact(n) / fact(n - r)
    print("Permutation: ", Permutation)
    Combination = fact(n) / (fact(r) * fact(n - r))
    print("Combination: ", Combination)
