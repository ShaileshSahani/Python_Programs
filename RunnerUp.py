# write a program to find the second winner in the array

if __name__ == "__main__":
    try:
        lis = list(map(int, input("Enter Values: ").split()))
        lis = sorted(set(lis))
        print("Runner Up: ", lis[-2])
    except Exception as e:
        print(e)
