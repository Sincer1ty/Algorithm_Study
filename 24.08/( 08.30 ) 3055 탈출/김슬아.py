# 미완성코드입니다..
from collections import deque
import sys
input=sys.stdin.readline
R,C=map(int,input().split())
forest=[list(input().strip()) for _ in range(R)]
# 고슴도치 위치 찾기
visited=[[False]*C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if forest[i][j]=="S":
            S=(i,j)
            visited[i][j]=True
        elif forest[i][j] =="*":
            water=(i,j)
time=0
dx=[1,-1,0,0]
dy=[0,0,1,-1]
queue=deque([S])
water_queue=deque([water])
while queue:
    # 고슴도치 위치부터 시작
    x,y =queue.popleft()
    # 굴 만나면 while문 빠져나오고 종료
    if forest[x][y]=="D":
        break
    # 상하좌우 이동
    count = 0
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0<=nx<R and 0<=ny<C and forest[nx][ny]!="X" and forest[nx][ny]!="*" and visited[nx][ny]==False:
             # 굴 도착하면 while문 탈출
            
            queue.append((nx,ny))
            visited[nx][ny]=True
        else:
           count+=1
    
    if count != 4 :
        w_x,w_y=water_queue.popleft()
        # 상하좌우 물 퍼짐
        for i in range(4):
                w_nx,w_ny = w_x+dx[i],w_y+dy[i]
                if 0<=w_nx<R and 0<=w_ny<C and forest[nx][ny]==".":
                    water_queue.append((w_nx,w_ny))
                    forest[w_nx][w_ny]="*"
        time+=1

print(time)
