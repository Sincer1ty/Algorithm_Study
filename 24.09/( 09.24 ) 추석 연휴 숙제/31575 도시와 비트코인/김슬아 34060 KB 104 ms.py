import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
city=[list(map(int,input().split()))for _ in range(M)]
dx=[0,1]
dy=[1,0]
queue=deque()
def bfs():
    for i in range(M):
        for j in range(N):
            if city[i][j]==1:
                queue.append((i,j))
                while queue:
                    x,y= queue.popleft()
                    if x==M-1 and y ==N-1:
                        return print("Yes")
                    city[x][y]=-1
                    for k in range(2):
                        nx,ny= dx[k]+x,dy[k]+y
                        if 0<= nx<M and 0<=ny<N and city[nx][ny]==1:
                            queue.append((nx,ny))
                            city[nx][ny]=-1
                return print("No")
bfs()
