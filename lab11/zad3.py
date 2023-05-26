def sortX(A, n):
    for j in range(n - 1, 0, -1):
        x = A[j]
        p = j
        k = n + 1
        while k - p>1:
            i = (p+k)//2
            if x <= A[i]:
                k = i
            else:
                p = 1
        for i in range(j, p):
            A[i] = A[i + 1]
        A[p] = x

lista = [0, 12, 3, 4, 10, 5, 11]
sortX(lista, 6)
print(lista)
