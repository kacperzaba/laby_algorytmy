def drukuj(array):
    print("--"*20)
    for i in range(len(array)):
        for j in range(len(array[i])):
            print(array[i][j], end="\t")
        print()

def newton_binomial(n, k):

    binomial = [[0 for j in range(k + 1)] for i in range(n + 1)]

    for i in range(n +1):
        binomial[i][0] = 1
    for j in range(k + 1):
        binomial[j][j] = 1

    for i in range(1, n + 1):
        for j in range(1, k+1):
            binomial[i][j] = binomial[i - 1][j - 1] + binomial[i - 1][j]
            print(i,j)
            drukuj(binomial)
    return binomial[n][k]

newton_binomial(4, 3)
