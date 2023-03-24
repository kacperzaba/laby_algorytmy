# Napisz program, który losuje 100 liczb całkowitych z przedziału -20, 50 i zapisuje je do tablicy dwuwymiarowej 10x10, następnie program znajdują maksymalną wartość w tej tablicy.

import random

# def create_two_dim_array(m, n):
#     lista = []
#     for i in range(m):
#         pom=[]
#         for j in range(n):
#             pom.append(random.randint(-20, 50))
#         lista.append(pom)
#     return lista


def create_two_dim_array(m, n):
    lista = [[random.randint(-20, 50) for i in range(n)] for j in range(m)]
    return lista

def print_two_dim_array(lista):
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            print(lista[i][j], end='\t')
        print()

macierz = create_two_dim_array(10, 10)
print_two_dim_array(macierz)

def find_max_elem_v2(lista):
    myMax = lista[0][0]
    for a in lista:
        for liczba in a:
            if liczba>myMax:
                myMax=liczba
    return myMax

def find_max_elem(lista):
    my_max = lista[0][0]
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if lista[i][j] > my_max:
                my_max = lista[i][j]
                row = i
                col = j
    return my_max, row, col

wynik = find_max_elem(macierz)
print(wynik)
print(f'maksymalny element wynosi {wynik[0]}, wiersz: {wynik[1]}, kolumna: {wynik[2]}')