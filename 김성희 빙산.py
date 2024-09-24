import sys
input = sys.stdin.readline

# 행과 열
N, M = map(int, input().split())

# 빙산 높이 저장
matrix = []
result = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))
    result.append([0] * M)

import queue

q = queue.Queue()

# 우, 좌, 상, 하
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def melt(source, dest):
    iceberg = []
    for x in range(N):
        for y in range(M):
            temp = source[x][y]
            if source[x][y] <= 0:     
                dest[x][y] = temp           
                continue
            for i in range(4):
                if x+dx[i] == -1 or y+dy[i] == -1 or x+dx[i] == N or y+dy[i] == M:
                    continue
                if source[x+dx[i]][y+dy[i]] <= 0:
                    temp -= 1
            dest[x][y] = temp
            if temp > 0:
                iceberg.append([x, y])
    return iceberg

import queue

q = queue.Queue()

# 한 덩어리인지 확인
def isOne(x, y, source, iceberg):
    visited = []
    for _ in range(N):
        visited.append([0] * M)
    
    q.put([x, y])
    visited[x][y] = 1

    while q.qsize():
        pos = q.get()
        x = pos[0]
        y = pos[1]

        for i in range(4):
            if x+dx[i] == -1 or y+dy[i] == -1 or x+dx[i] == N or y+dy[i] == M:
                continue
            if source[x+dx[i]][y+dy[i]] > 0 and visited[x+dx[i]][y+dy[i]] == 0:
                iceberg.pop()
                q.put([x+dx[i], y+dy[i]])
                visited[x+dx[i]][y+dy[i]] = 1
    
    if len(iceberg):
        return 0
    return 1

count = 0
sample = []
while 1:
    if count % 2 == 0:
        sample = melt(matrix, result)
        pos = sample.pop()
        if not isOne(pos[0], pos[1], result, sample):
            count += 1
            break
    else:
        sample = melt(result, matrix)
        pos = sample.pop()
        if not isOne(pos[0], pos[1], matrix, sample):
            count += 1
            break
    count += 1

# while 한 덩어리가 아니면 melt()
# 반복 횟수가 답

print(count)
