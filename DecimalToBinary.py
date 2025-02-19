dec_number = int(input("Enter a number: "))
temp = dec_number
num_list = []
while dec_number > 0:
    num_list.append(int(dec_number % 2))
    dec_number //= 2
print(f"Binary number for {temp} is ", end="")
for i in num_list[::-1]:
    print(i, end=" ")
