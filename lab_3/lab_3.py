# Napisz program, który mnoży dwie tablice n -wymiarowe przez siebie.
# Jakie muszą być spełnione założenia przy mnożeniu dwóch tablic dwuwymiarowych?
# Jaka jest złożoność obliczeniowa takiego programu?

def create_two_dim_array(m, n):
    lista = [[random.randint(-20, 50) for i in range(n)] for j in range(m)]
    return lista

a = create_two_dim_array(5, 4)
b = create_two_dim_array(4, 5)

def mulMatrix(m1, m2):
    wm1 = len(m1)
    km1 = len(m1[0])
    wm2 = len(m2)
    km2 = len(m2[0])
    if wm1==km2 and km1==wm2:
        m3 = []
        for i in range(wm1):
            pom = []
            for j in m1:
                for c in m2:
                    w+=j*c