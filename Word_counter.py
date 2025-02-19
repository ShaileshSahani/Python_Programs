from collections import Counter


def sep_string(s: str):
    return s.split()


def counter_string(lis: list):
    dic: dict = {}
    for i in lis:
        dic[i] = 0
    for i in dic.keys():
        for s in lis:
            if i == s:
                dic[i] = dic.get(i) + 1
    for s in dic.keys():
        print(f"{s} : {dic.get(s)} times")


def count(lis: list):
    m = Counter(lis)
    for key, item in m.items():
        print(f"{key} : {item} times")


input_string = input("Enter a string: ")
get_list = sep_string(input_string.strip())
counter_string(get_list)
count(get_list)
