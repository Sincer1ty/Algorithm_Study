# 최적화 코드
from collections import deque
import sys
input=sys.stdin.readline
# 토마토 상자의 가로 세로 높이 값 받음
M,N,H=map(int,input().split())
# 토마토 넣음
boxes=[list(map(int,input().split())) for _ in range(N*H)]
# 2차원배열이라 세로 높이를 곱해줌
all_row=N*H
# 하 상 우 좌 위 아래 이동 배열
dx=[1,-1,0,0,N,-N]
dy=[0,0,1,-1,0,0]
# 익은 토마토의 위치를 넣을 큐
ripen_tomatos=deque()
# 안 익은 토마토 개수
unripe = 0
# 입력받은 초기 토마토 상자의 익은 토마토 위치 넣음
for i in range(all_row):
    for j in range(M):
        if boxes[i][j] ==1:
            ripen_tomatos.append((i,j))
        if boxes[i][j] ==0:
            unripe+=1
# 초기 토마토 상자 안 토마토가 모두 익은 상태일 경우 안익혀도되므로
if unripe ==0:
    print(0)
else:
    day=-1
    while ripen_tomatos:
        day+=1
        for _ in range(len(ripen_tomatos)):
            x,y = ripen_tomatos.popleft()
            for i in range(6):
                # x,y 가 층의 경계에 있는 지 확인 ,경계에 있으면 위 아래 1로 바꾸지 x
                if (i == 0 and x%N == N-1) or (i == 1 and x%N == 0):
                    continue
                nx,ny = dx[i]+x,dy[i]+y
                if 0<=nx<all_row and 0<=ny<M and boxes[nx][ny]==0:
                        boxes[nx][ny]=1
                        ripen_tomatos.append((nx,ny))
                        unripe-=1
    # 익힌 토마토 다 돌고 상자에 안익은 토마토가 하나도 없으면 day 출력 
    # 다 돌았는데도 안익은 토마토가 있으면 -1 출력 
    print(day if unripe==0 else -1)



# 원래 제출한 코드
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
