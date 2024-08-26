import sys
input = sys.stdin.readline

class Node:
    def __init__(self, val):
        self.adj = []
        self.val = val
        self.color = "white"
        self.u = None
        
K = int(input())

def dfs(graph, v):
    if v.color == 'gray':
        return 

    v.color = 'gray'
    print(v.val, end=' ')
    count += 1
    for a in v.adj:
        if a in graph:
            dfs(a)
        
    return count

for _ in range(K):
    V, E = map(int, input().split())
    
    vertex = [Node(i+1) for i in range(V)]
    for _ in range(E):
        edge = list(map(int, input().split()))
        vertex[edge[0]-1].adj.append(vertex[edge[1]-1])
        vertex[edge[1]-1].adj.append(vertex[edge[0]-1])

    group = []
    
    group.append(vertex.pop(vertex[0].adj[0].val -1))

    dfs(vertex, vertex[0])
    dfs(group, group[0])

