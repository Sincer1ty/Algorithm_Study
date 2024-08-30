import sys
input = sys.stdin.readline

R, C = map(int, input().split())

map = []
water = []
stone = []
for _ in range(R):
    row = list(input().strip())
    for i, r in enumerate(row):
        if r == 'D':
            dest = (_, i)
        elif r == 'S':
            start = (_, i)
        elif r == '*':
            water.append((_, i))
        elif r == 'X':
            stone.append((_, i))
    map.append(row)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# D : 비버의 굴 (도착지)
# S : 출발지
# * : 물 (매분 상하좌우로 확장 - 비어있을 때)
# X : 돌

import queue

q = queue.Queue()

def bfs(x,y):

    q.put([x,y])
    
    while q.qsize():
        pos = q.get()
        x = pos[0]
        y = pos[1]

        for i in range(4):
            if map[x+dx[i]][y+dy[i]] == 1:
                map[x+dx[i]][y+dy[i]] += map[x][y]
                q.put([x+dx[i], y+dy[i]])
        map[1][1] = 0

bfs(start[0], start[1])


for i in range(R, -1, -1): # 행
    for j in range(C, -1, -1): # 열

        for k in range(4):
            x = i+k
            y = j+k
            map[x][y]
            pass
