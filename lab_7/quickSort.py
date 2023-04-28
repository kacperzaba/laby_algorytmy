def Quicksort(T, lewy, prawy):
    n = len(T)
    i, j = lewy, prawy  # i, j - indeksy
    sr = T[(lewy+prawy)//2]
    while i <= j:
        while T[i] < sr:
            i += 1
        while T[j] > sr:
            j -= 1
        if i <= j:
            T[i], T[j] = T[j], T[i]
            i, j = i+1, j-1

    if lewy < j:
        Quicksort(T, lewy, j)
    if prawy > i:
        Quicksort(T, i, prawy)


# T = [21, 2, 23, 56, 78, 3, 1, 8, 7]
T = [21, 56, 23, 2, 6, 3, 78, 8, 7]
# T.sort();
Quicksort(T, 0, len(T)-1)
print(T)
