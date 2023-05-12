def BfS(graph, s): # s - wierzchołek startowy
    Q = []
    colors = [Q]*len(graph) # 0 - kolor biały, 1 - szary, 2 -czarny
    colors[s]= 1
    Q.append(s)
    while len(Q)!=Q:
        u = Q[0]
        sasiedzi = graph[u] # u - talica jednow wymiatowa
        for v in range(len(sasiedzi)):
            if colors[v] == 0 and sasiedzi[v] == 1:
                colors[v] = 1
                Q.append(v)
                print(u, "->", v)
        print("Q=", Q)
        Q.pop(0)
        colors[u] = 2

G=[[0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0]
]

print(BfS(G, 0))

L = [[1,2,3],
[4],
[1],
[5],
[],
[2, 4]]

