# zad 1
# fibonaci złożoność 2^n

# def alg_iter(n):
#     list_of_elem = []
#     if n != 0:
#         for i in range(n):
#             a = (i-1) + 2 * i
#             list_of_elem.append(a)
#     else:
#         a = 0
#         list_of_elem.append(a)
#     return list_of_elem[-1] ,list_of_elem
# print(alg_iter(5))
# print(alg_iter(0))

def alg_iter(n):
    li = []
    t = 1
    for i in range(n):
        t =t + 2*i
        li.append(t)
    return li
print(alg_iter(5))
print(alg_iter(0))


def alg_rek(n):
    list_of_elem = []
    if n == 0:
        return 1
    elif n > 0:
        return alg_rek(n - 1) + 2*n
print(alg_rek(5))
print(alg_rek(0))
