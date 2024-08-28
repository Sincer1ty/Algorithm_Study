# 통과한 것으로 업뎃합니다
from collections import deque
import sys
input = sys.stdin.readline
K =int(input())
for _ in range(K):
    V,E =map(int,input().split())
    graph=[[] for _ in range(V+1)]
    for _ in range(E):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    # 컬러체크리스트만듬 0을 방문리스트로 쓰고 1,-1을 각각 다른 색으로 간준
    color = [0]*(V+1)
    checkBipartiite= True

    for i in range(1,V+1):
        if color[i]!=0:
            continue
        queue=deque()
        queue.append(i)
        # 컬러 1로 시작 -1으로 시작해도 상관없음
        color[i]=1
        while queue:
            vertex=queue.popleft()
            for j in graph[vertex]:
                if color[vertex] == color[j]:
                    checkBipartiite= False
                    break
                if color[j]==0:
                    queue.append(j)
                    color[j]=color[vertex]*-1
    if checkBipartiite:
        print("YES")
    else:
        print("NO")
    
    
