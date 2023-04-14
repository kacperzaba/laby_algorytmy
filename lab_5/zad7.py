# Zaproponuj rekurencyjny algorytm przeliczania liczby w dowolnym systemie od 2 do 9 na liczbę binarną.
def bin_to_dec(tekst, x):
    n = len(tekst)
    wynik = ord(tekst[0])-48 # odejmuje 48 bo to zamiana z kodu ascii
    for i in range(1, n):
        wynik = wynik * x + ord(tekst[i])-48
    return wynik

print(bin_to_dec('101', 2))


def bin_to_hex_or_dec(tekst, x):
    lista = '0123456789ABCDEF'
    wynik = lista.find(tekst[0])
    n = len(tekst)
    for i in range(1, n):
        wynik = wynik * x + lista.find(tekst[i])
    return wynik

print(bin_to_hex_or_dec('101',2))
print(bin_to_hex_or_dec('C2',16))


def bin_to_dec_rek(tekst, x):
    if len(tekst) == 1:
        return ord(tekst[0])-48
    else:
        return x * bin_to_dec_rek(tekst[0:len(tekst)-1], x) + ord(tekst[len(tekst)-1])-48
print(bin_to_dec_rek('101', 2))

def bin_to_hex_rek(tekst,x):
    lista = '0123456789ABCDEF'
    if len(tekst) == 1:
        return lista.find(tekst[0])
    else:
        return x * bin_to_hex_rek(tekst[0:len(tekst)-1],x) + lista.find(tekst[len(tekst)-1])

print(bin_to_hex_rek('C2', 16))