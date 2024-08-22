# 완전히 다 보고 함 
# 회전하는 함수를 만들기 위해서, dx, dy를 오른쪽, 밑, 왼쪽, 위로 이동하는 형태로 만드는 과정이 연상하기가 너무 어려움 

from collections import deque
import sys

read = sys.stdin.readline

n = int(read().strip())
app_k = int(read().strip())

graph = [[0]*n for _ in range(n)]

for i in range(app_k):
    p,q = map(int ,read().strip().split())
    graph[p-1][q-1] = 1


t = int(read().strip())
turn = []
for i in range(t):
    x, chrt = map(str, read().strip().split())
    turn.append((int(x), chrt))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

idx, nx, ny = 0, 0, 0
time, q = 0, 0

queue = deque()
queue.append((nx, ny))

while True:
    nx = nx + dx[idx]
    ny = ny + dy[idx]
    time +=1

    # 전체 보드를 넘어가거나, 이미 큐에 포함이 돼 있을 경우
    if nx < 0 or nx >=n or ny < 0 or ny >= n  or (nx, ny) in queue:
        break

    queue.append((nx, ny))

    # 보드에 사과가 없다면, 그 이전 위치의 좌표를 pop해서 없애준다.
    if graph[nx][ny] ==0:
        queue.popleft()
    
    # 보드에 사과가 있다면, 해당되는 좌표를 0으로 바꿔준다.
    else:
        graph[nx][ny] = 0

    # 현재 시간과 회전하는 시간이 일치할 경우, 회전하는 함수를 실행 
    if time == turn[q][0]:
        if turn[q][1]== 'L':
            idx = (idx -1) %4
        else:
            idx = (idx + 1) % 4
        #회전할 횟수가 남아 있다면, 그 다음 회전하는 인덱스로 증가시킨다.
        if q + 1 < len(turn):
            q +=1


print(time)


