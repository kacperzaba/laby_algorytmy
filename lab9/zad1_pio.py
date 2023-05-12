def BFS_for_graph(graph, s):
    Q = []
    colors = [0]* len(graph) # 0 - kolor biały(nie odwiedzony wierzchołei), 1 - szary(w kolejce), 2 - czarny()
    colors[s] = 1
    Q.append(s)
    while len(Q) > 0:
        u = Q[0]
        sasiedzi = graph[u]
        for v in range (len(sasiedzi)):
            if colors[v] == 0 and sasiedzi[v] == 1:
                colors[v] = 1
                Q.append(v)
        print("Q = ", Q)
        Q.pop(0)
        colors[u] = 2

# def BFS_for_list(graph, s):


G = [ [0, 1, 1, 1, 0, 0], # gfraf jest w prezentacji, jedynki są tam gdzie mozemy przejsc z konkretnego node'a, kazda tablica przedstawia node od 0 do 5
      [0, 0, 0, 0, 1, 0],
      [0, 1, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 1],
      [0, 0, 0, 0, 0, 0],
      [0, 0, 1, 0, 1, 0]
    ] 

BFS_for_graph(G, 0)

print(BFS_for_graph(G, 0))

L = [[1,2,3],
[4],
[1],
[5],
[],
[2, 4]]

def BFS_for_list(lista, s):
    Q = []
    colors = [0]* len(lista) # 0 - kolor biały
    colors[s] = 1
    Q.append(s)
    while len(Q) > 0:
        u = Q[0]
        sasiedzi = lista[u]
        for v in sasiedzi:
            if colors[v] == 0:
                colors[v] = 1
                Q.append(v)
        print("Q = ", Q)
        Q.pop(0)
        colors[u] = 2
BFS_for_list(L,0)


