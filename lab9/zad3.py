def DFS_for_graph(graph, s):
    Stos = []
    colors = [0]* len(graph) # 0 - kolor biały(nie odwiedzony wierzchołei), 1 - szary(w kolejce), 2 - czarny()
    colors[s] = 1
    Stos.append(s)
    while len(Stos) > 0:
        u = Stos[-1]
        sasiedzi = graph[u]
        Stos.pop()
        for v in range (len(sasiedzi)):
            if colors[v] == 0 and sasiedzi[v] == 1:
                colors[v] = 1
                Stos.append(v)
        print("Q = ", Stos)
        colors[u] = 2

G=[[0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0]
]
DFS_for_graph(G, 0)