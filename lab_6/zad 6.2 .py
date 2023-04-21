a = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
# l - lewa
# p - prawa
# def divandcong(a):
#     liczba_zer = 0
#     k = 0
#     k = len(a) - 1
#     while p <= k:
#         s = (p + k) // 2
#         if a[s] == 1:
#             k = s - 1
#         else:
#             liczba_zer = liczba_zer + (s - p) + 1
#             p = s + 1
#     return liczba_zer


def divandcong(a):
    liczba_zer = 0
    p = 0
    k = len(a)-1
    while p <= k:
        sr = (p+k)//2
        if a[sr] == 1:
            k = sr - 1
        else:
            liczba_zer = liczba_zer + (sr-p) + 1
            p = sr + 1
    return liczba_zer

print(divandcong(a))