from collections import deque
import sys
input=sys.stdin.readline
N,M = map(int,input().split())
Antartica =[list(map(int,input().split())) for _ in range(N)]
iceberg_queue=deque()
separate_queue=deque()
for i in range(N):
    for j in range(M):
        if Antartica[i][j]>0:
            iceberg_queue.append((i,j))
dx=[0,0,1,-1]
dy=[1,-1,0,0]
isSeparated=False
separatedTime=0
while iceberg_queue:
    if isSeparated:
        break
    visited = [[False]*M for _ in range(N)]
    for _ in range(len(iceberg_queue)):
        x,y=iceberg_queue.popleft()
        visited[x][y]=True
        cnt=0
        for i in range(4):
            nx,ny=dx[i]+x,dy[i]+y
            if 0<=nx<N and 0<=ny<M and visited[nx][ny]==False:
                if Antartica[nx][ny]<=0:
                    cnt+=1
        Antartica[x][y]-=cnt
        if Antartica[x][y]>0:
            iceberg_queue.append((x,y))
    separatedTime+=1
    if not iceberg_queue:
        break
    else:
        cnt2=0
        separate_queue.append(iceberg_queue[0])
        while separate_queue:
            x,y=separate_queue.popleft()
            visited[x][y]=False
            cnt2+=1
            for i in range(4):
                nx,ny=dx[i]+x,dy[i]+y
                if Antartica[nx][ny]>0 and visited[nx][ny]==True:
                    separate_queue.append((nx,ny))
                    visited[nx][ny]=False
        if len(iceberg_queue)!=cnt2:
            isSeparated=True
if isSeparated:
    print(separatedTime)
else:
    print(0)
