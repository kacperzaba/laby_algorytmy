# Napisz program, który mnoży tablicę dwuwymiarową przez dowolna liczbę podaną z klawiatury.

import random

def create_two_dim_array(m, n):
    lista = [[random.randint(-20, 50) for i in range(n)] for j in range(m)]
    return lista

macierz = create_two_dim_array(5, 3)
print(macierz)
def muit_list_by_number(lista, number):
    for a in range(len(lista)):
        for j in range(len(lista[a])):
            lista[a][j] = lista[a][j]*number
    return lista
print(muit_list_by_number(macierz, 3))

# a = [1, 2, 3, 4]
# a = [i*3 for i in a]
# print(a)
