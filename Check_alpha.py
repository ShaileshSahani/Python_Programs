import string


def is_pan(sen, alphabet=string.ascii_lowercase):
    print(string.ascii_lowercase)
    return set(sen) >= set(alphabet)


print(is_pan(string.ascii_lowercase))
