if __name__ == "__main__":
    n = int(input("Enter The Number Of Student: "))
    dic = {}
    for i in range(n):
        name, *marks = input().split()
        score = list(map(int, marks))
        dic[name] = score
    print(dic)
    try:
        x = input("Enter Student Name: ")
        s = dic[x]
        ad = sum(s)
        avg = ad / len(s)
        print(round(avg, 2))
    except Exception as e:
        print(e)