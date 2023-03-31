# Dana jest iteracyjna wersja funkcji znajdowania NWD.

# def nwd_i(a, b):
#     while b:
#         a, b = b, a%b
#     return a
# return m; }

# Zdefiniuj rekurencyjna funkcję znajdowania NWD wykorzystując operator reszty z dzieelnia.

def pisz(tekst, n):
    for i in range(n):
        print(tekst)

def pisz_rek(tekst,n):
    if n>0:
        print(tekst)
        pisz_rek(tekst, n-1)
        # najprostasza funkcja rekurencyjna
# pisz_rek("algorytmy", 10)

def silnia_iter(n):
    s = 1
    for i in range(1, n + 1):
        s = s * i
    return s

# print(silnia_iter(3))

def silnia_rek(n):
    if n==0 or n==1:
        return
    else:
        return n*silnia_iter(n-1)
print(silnia_iter(20))
print(silnia_rek(20))