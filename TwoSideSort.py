# TODO
my_list = [2, 9, 4, 7, 3, 8, 10, 9]
# OUT
# [2, 4, 7, 9, 10, 9, 8, 3]
print(f"Current List: {my_list}")


def method1(lis):
    half = len(lis) // 2
    l_ = sorted(lis[:half:], reverse=False)
    r_ = sorted(lis[half::], reverse=True)
    print('Normal = ', l_ + r_)


method1(my_list)


def dsa_method(lis):
    half = len(lis) // 2
    l_ = bubble_sort(lis[:half:], 'asc')
    r_ = bubble_sort(lis[half::], 'desc')
    print('Dsa = ', l_ + r_)


def bubble_sort(lis, method):
    for i in range(len(lis)):
        for j in range(len(lis)):
            if method == 'asc':
                if lis[i] < lis[j]:
                    temp = lis[i]
                    lis[i] = lis[j]
                    lis[j] = temp
            elif method == 'desc':
                if lis[i] > lis[j]:
                    temp = lis[i]
                    lis[i] = lis[j]
                    lis[j] = temp
    return lis


dsa_method(my_list)
