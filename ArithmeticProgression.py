start = int(input("Enter Starting point: "))
end = int(input("Enter Ending Point: "))
common_def = int(input("Enter Common Difference: "))
print("The AP Series: ", end=" ")
for i in range(start, end, common_def):
    print(i, end=" ")

