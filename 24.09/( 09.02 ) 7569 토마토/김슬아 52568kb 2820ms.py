from collections import deque
import sys
input=sys.stdin.readline

M,N,H=map(int,input().split())

boxes=[list(map(int,input().split())) for _ in range(N*H)]
all_row=N*H
def all_ones(matrix):
    return all(all(element == 1 for element in row) for row in matrix)
if any(0 in row for row in boxes):
    dx=[1,-1,0,0,N,-N]
    dy=[0,0,1,-1,0,0]
    ripen_tomatos=deque()
    for i in range(all_row):
        for j in range(M):
            if boxes[i][j] ==1:
                ripen_tomatos.append((i,j))
    day=0
    while ripen_tomatos:
        for _ in range(len(ripen_tomatos)):
            x,y = ripen_tomatos.popleft()
            for i in range(6):
                nx,ny = dx[i]+x,dy[i]+y
                if i == 0 and x%N == N-1:
                    continue
                if i == 1 and x%N == 0:
                    continue
                if 0<=nx<all_row and 0<=ny<M and boxes[nx][ny]==0:
                        boxes[nx][ny]=1
                        ripen_tomatos.append((nx,ny))
        day+=1
    if any(0 in row for row in boxes):
        print(-1)
    else:
        print(day-1)
else:
    print(0)
