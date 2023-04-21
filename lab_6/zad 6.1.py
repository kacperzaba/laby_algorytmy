# dziel i zwycięzaj
# 1. muszą być posortowane
# to na zaliczenie

a = [3, 7, 21, 31, 35, 45, 51, 60]
def binary_search_iter(a, elem):
    p = 0
    k = len(a) - 1
    while p <= k:
        srodek = (p + k) // 2
        if a[srodek] == elem:
            return srodek
        elif a[srodek] < elem:
            p = srodek + 1
        else:
            k = srodek - 1 
    return False

# print(binary_search_iter(a, 3))


def binary_search_rek(a, elem, poczatek, koniec):
    srodek = (poczatek + koniec) // 2
    if poczatek > koniec:
        return False
    elif a[srodek] == elem:
        return srodek
    elif a[srodek] > elem:
        return binary_search_rek(a, elem, 0, srodek -1)
    else:
        return binary_search_rek(a, elem, srodek + 1, koniec)

print(binary_search_rek(a, 51, 0, len(a)-1))