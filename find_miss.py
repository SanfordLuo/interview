def find_miss():
    for a in range(1, len(A) + 2):
        if a not in A:
            return a
A = [2, 5, 7, 8, 9, 3, 4, 6, 10]
print(find_miss())


def func():
    for b in range(1, len(B) + 2):
        if B[b - 1] != b:
            return b
B = [2, 1, 12, 7, 8, 9, 11, 3, 4, 6, 10]
B.sort() # reverse
print(func())


C = [2, 1, 12, 7, 8, 9, 11, 3, 4, 6, 10]
my_c = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
set_c = set(C)
print(my_c - set_c)


