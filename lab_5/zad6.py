# Zaproponuj rekurencyjny algorytm szybkiego potęgowania.
def potega(a, b):
    if b==1:
        return a
    elif b==0:
        return 1
    else:
        return a*potega(a,b-1)


def potega_rek(a, b):
    if b==1:
        return a
    elif b%2==0:
        s = potega_rek(a, b/2)
        return s*s
    else:
        return potega_rek(a,b-1)

