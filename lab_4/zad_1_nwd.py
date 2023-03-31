def nwd_i(a, b):
    while b:
        a,b = b, a%b
        # jeżeli pierwsza liczba jest mniejsza to program to odwróci
    return a

def nwd_r(a,b):
    if b != 0:
        return nwd_r(b, a%b)
    else:
        return  a

print(nwd_r(24, 36))
print(nwd_i(24, 36))

def nwd_iter(a, b):
    while b != a:
        if a > b:
            a = a - b
        else:
            b = b - a
    
    return b

print(nwd_iter(24, 36))

def nwd_rek(a,b):
    if a==b:
        return a
    elif a>b:
        return nwd_rek(a-b, b)
    else:
        return nwd_rek(a, b-a)

print(nwd_rek(24, 36))