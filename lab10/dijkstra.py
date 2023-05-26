import sys

G = [
    [0, 10, 3, 0, 0],
    [0, 0, 1, 2, 0], 
    [0, 4, 0, 8, 2], 
    [0, 0, 0, 0, 7], 
    [0, 0, 0, 8, 0]
]

dist=[sys.maxsize] * len(G)
print(dist)

def dijkstra(graph, dist, start):
    dist[start] = 0
    S = []
    Q = []
    for i in range(len(graph)):
        Q.append(i)
    while len(Q) > 0:
        u = mindistance(dist, S)