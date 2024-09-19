import sys
input = sys.stdin.readline

N = int(input())

home = []
for _ in range(N):
    home.append(list(map(int, input().strip())))

# 우, 좌, 상, 하
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

import queue

q = queue.Queue()

visited = []
for _ in range(N):
    visited.append([0] * N)

count_list = []
def bfs(x, y):
    home[x][y] = 0
    q.put([x, y])
    visited[x][y] = 1
    count = 1

    while q.qsize():
        pos = q.get()
        x = pos[0]
        y = pos[1]

        for i in range(4):
            if x+dx[i] == -1 or y+dy[i] == -1 or x+dx[i] == N or y+dy[i] == N:
                continue
            if home[x+dx[i]][y+dy[i]] == 1 and visited[x+dx[i]][y+dy[i]] == 0:
                home[x+dx[i]][y+dy[i]] = 0
                q.put([x+dx[i], y+dy[i]])
                visited[x+dx[i]][y+dy[i]] = 1
                count+=1
    return count

for x in range(N):
    for y in range(N):
        if home[x][y] == 1 and visited[x][y] == 0:
            count_list.append(bfs(x, y))

count_list.sort()  # 오름차순 정렬

print(len(count_list))
for c in count_list:
    print(c)
