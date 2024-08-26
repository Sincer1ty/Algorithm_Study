from collections import deque
K =int(input())
RED=1
BLUE=-1
for i in range(K):
    V,E =map(int,input().split())
    graph=[set() for _ in range(V+1)]
    for _ in range(E):
        u,v = map(int,input().split())
        graph[u].add(v)
        graph[v].add(u)
    color = [0]*(V+1)
    checkBipartiite= True

    def bfs(s,color):
        queue=deque([s])
        color[s]=color
        while queue:
            vertex=queue.popleft()
            for i in graph[vertex]:
                if color[i]==0:
                    queue.append(i)
                    color[i]=color[vertex]*-1
                elif color[vertex] + color[i] !=0:
                    checkBipartiite= False
                    return
  
    for i in range(V+1) :
    #  이분 그래프가 아니면 반복문 탈출
        if not checkBipartiite:
            break
        if color[i] == 0:
            bfs(i, RED)
    if checkBipartiite:
        print("YES")
    else:
        print("NO")
