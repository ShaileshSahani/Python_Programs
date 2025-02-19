def search_vowel(string):
    for i in string:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            print("Vowel:", i)


string1 = "i am hello".lower()
search_vowel(string1)
