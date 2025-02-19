def split_words(s: str):
    word_lists = s.split(' ')
    return word_lists

def compare_length(words: list):
    longest_word = words[0]
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

x = input("Enter a sentence: ")
y = split_words(x.strip())
print("The largest word is:", compare_length(y))

