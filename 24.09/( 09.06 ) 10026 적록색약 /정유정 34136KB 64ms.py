import sys
from collections import deque

size = int(sys.stdin.readline())
graph = []
for _ in range(size):
    graph.append(list(map(str, sys.stdin.readline().strip())))

is_visited = [[False] * size for _ in range(size)]
queue = deque()
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def red_green_bfs() -> int:
    cnt = 0

    for i in range(size):
        for j in range(size):
            if is_visited[i][j]:
                continue

            queue.append((i, j))
            is_visited[i][j] = True
            while queue:
                cur_y, cur_x = queue.popleft()

                for k in range(4):
                    mx = cur_x + dx[k]
                    my = cur_y + dy[k]

                    if mx < 0 or mx >= size or my < 0 or my >= size or is_visited[my][mx]:
                        continue
                    if (graph[cur_y][cur_x] == graph[my][mx] or
                            (graph[cur_y][cur_x] in ('R', 'G') and graph[my][mx] in ('R', 'G'))):
                        queue.append((my, mx))
                        is_visited[my][mx] = True

            cnt += 1
    return cnt


def bfs() -> int:
    cnt = 0

    for i in range(size):
        for j in range(size):
            if is_visited[i][j]:
                continue

            queue.append((i, j))
            is_visited[i][j] = True
            while queue:
                cur_y, cur_x = queue.popleft()

                for k in range(4):
                    mx = cur_x + dx[k]
                    my = cur_y + dy[k]

                    if mx < 0 or mx >= size or my < 0 or my >= size:
                        continue
                    if not is_visited[my][mx] and graph[cur_y][cur_x] == graph[my][mx]:
                        queue.append((my, mx))
                        is_visited[my][mx] = True

            cnt += 1
    return cnt


people = bfs()
queue.append((0, 0))
is_visited = [[False] * size for _ in range(size)]
rg_people = red_green_bfs()
sys.stdout.write(str(people) + " " + str(rg_people))
