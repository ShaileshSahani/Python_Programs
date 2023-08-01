n1 = input()
n = ''
for i in n1:
    if (i.isupper()) is True:
        n += (i.lower())
    else:
        n += (i.upper())
print(n)
