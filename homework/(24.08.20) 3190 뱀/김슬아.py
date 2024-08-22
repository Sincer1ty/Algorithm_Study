from collections import deque

# 입력 받기
N = int(input())  # 보드의 크기
K = int(input())  # 사과의 개수
apples = set()
# 사과 위치 입력 받기
for i in range(K):
    x,y = map(int,input().split())
    apples.add((x,y))
L = int(input())  # 방향 변환 횟수
directions = {}
# 방향 변환 정보 입력 받기
for i in range(L):
    time,dir = input().split()
    directions[int(time)] =dir
# 방향 정의 (동, 남, 서, 북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

snake = deque([(1,1)])  # 뱀의 위치
# 방향: 0(동), 1(남), 2(서), 3(북)
direction = 0  # 초기 방향
time = 0
# 메인 게임 루프

def turn(C):
    global direction
    # 방향 전환 로직 구현
    # 빙향값이 항상 0123중 하나가 되도록 보장 하는 연산임
    if C=="L":
        direction=(direction-1)%4
    if C=="D":
        direction=(direction+1)%4

def is_game_over(head):
    # 게임 종료 조건 체크 로직 구현
    # 벽 충돌 체크
    if head[0] <1 or head[0] > N or head[1] < 1 or head[1] > N:
        return True
    # 자기 자신과 충돌 체크
    if head in list(snake)[1:]:
        return True
    return False
def move_snake():
    # 뱀 이동 로직 구현
    global snake, apples
    # 뱀 머리 위치 계산
    head=snake[0]
    new_head = (head[0] + dx[direction],head[1]+dy[direction])
    # 새로운 머리 위치를 뱀에 추가
    snake.appendleft(new_head)

    if new_head in apples:
        apples.remove(new_head)
    else:
        snake.pop()
    return new_head

while True:
    time += 1
    
    # 뱀 이동
    new_head=move_snake()
    
    # 게임 종료 체크
    if is_game_over(new_head):
        break
    
    # 사과 처리
    # 사과를 먹었을 때와 먹지 않았을 때의 로직 구현
    
    # 방향 변환 처리
    if time in directions:
        turn(directions[time])

# 결과 출력
print(time)
