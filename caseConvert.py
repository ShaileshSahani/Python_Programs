class CaseChange:
    string = input("Enter any string: ")
    null_str = ""
    for i in string:
        if i.isupper() is True:
            null_str += i.lower()
        else:
            null_str += i.upper()
    print("Old Str: ", string)
    print("New String: ", null_str)
