import sys
input = sys.stdin.readline

N=int(input())

# 사과 받기
K=int(input())
apple=[[False for _ in range(N)] for _ in range(N)]
for _ in range(K):
    a, b = map(int,input().split())
    apple[a-1][b-1] = True

# 방향 변환 정보 받기
L = int(input())
dir = []
for _ in range(L):
    dir.append(list(input().split()))
dir.append([0,0])

# 오른쪽으로 방향 90도 회전
# (0,1) -> (1,0)
# (1,0) -> (0,-1)
# (0,-1) -> (-1,0)
# (-1,0) -> (0,1)

# 방향 변환 정보는 0이 될 때까지 계속 확인,
# 시간이 일치하면 방향을 바꾸고 다음 인덱스로 넘어감
def changeDirection(direction, time):
    global idxD
    if int(direction[0]) == time:
        # 오른쪽으로 방향 회전
        if direction[1] == 'D':
            idxD += 1
            return 1
        else:
            idxD += 1
            return -1
    else:
        return 0

from collections import deque
# 꼬리는 가장 처음 들어간 값

# heading만큼 좌표를 더해준 후에
# 게임이 끝났는지 확인하고
# 사과를 못 먹었다면 꼬리를 삭제한다
# 시간을 더해준다
# 방향을 바꿔준다

# 방향을 관리하는 정보들
heading = [[0,1],[1,0],[0,-1],[-1,0]]
idxH = 0
idxD = 0
# 꼬리부터 큐로 들어간다
body = deque()
bodyArr = [[False for _ in range(N)] for _ in range(N)]
body.append([0,0])
time = 0

while(1):
    head = [body[-1][0] + heading[idxH%4][0], body[-1][1] + heading[idxH%4][1]]
    body.append(head)
    # 시간을 더해준다
    time += 1
    # 벽에 부딪히면 종료
    if not ((0 <= head[0] < N) and (0 <= head[1] < N)):
        break
    # 자기 몸에 부딪히면 종료
    if bodyArr[head[0]][head[1]] == True:
        break
    bodyArr.append(head)
    bodyArr[head[0]][head[1]] = True
    # 사과가 없으면 꼬리 삭제
    if not apple[head[0]][head[1]]:
        bodyArr[body[0][0]][body[0][1]] = False
        body.popleft()
    else:
        apple[head[0]][head[1]] = False
    # 방향을 바꿔준다
    idxH += changeDirection([dir[idxD][0],dir[idxD][1]],time)
    
print(time)



    

