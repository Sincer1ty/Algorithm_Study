import sys
from collections import deque
input=sys.stdin.readline
N=int(input())
colors = [list(input().strip()) for _ in range(N)]
same_color_queue=deque()
diff_color_queue=deque()
            
# print(colors)

dx=[1,-1,0,0]
dy=[0,0,1,-1]
same_color_queue.append((0,0))
visited=[[False]*N for _ in range(N)]
count = 0
while (1):
    if not same_color_queue:
        x,y=diff_color_queue.popleft()
        count+=1
    else:
        x,y=same_color_queue.popleft()
    visited[x][y]=True
    if x==N-1 and  y==N-1:
        break
    for i in range(4):
        nx,ny = dx[i]+x,dy[i]+y
        if 0<=nx<N and 0<=ny<N  and visited[nx][ny]==False:
            if colors[x][y]==colors[nx][ny]:
                same_color_queue.append((nx,ny))
             
                visited[nx][ny]=True
            else:
                if (x,y) in diff_color_queue:
                    diff_color_queue.remove((x,y))
                diff_color_queue.append((nx,ny))





