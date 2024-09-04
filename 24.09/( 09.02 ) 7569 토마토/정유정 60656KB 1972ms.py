import sys
from collections import deque

c, r, h = map(int, sys.stdin.readline().strip().split())
box = [[] for _ in range(h)]
is_visited = [[[False] * c for _ in range(r)] for _ in range(h)]
queue = deque()
for i in range(h):
    for j in range(r):
        check = list(map(int, sys.stdin.readline().strip().split()))
        box[i].append(check)
        for idx in range(c):
            if check[idx] == 1:
                queue.append([i, j, idx])
                is_visited[i][j][idx] = True


def bfs() -> None:
    while queue:
        cur = queue.popleft()
        dh = [-1, 1, 0, 0, 0, 0]
        dy = [0, 0, -1, 1, 0, 0]
        dx = [0, 0, 0, 0, -1, 1]

        for i in range(6):
            mh = dh[i] + cur[0]
            my = dy[i] + cur[1]
            mx = dx[i] + cur[2]

            if mh < 0 or mh >= h or my < 0 or my >= r or mx < 0 or mx >= c:
                continue

            if not is_visited[mh][my][mx] and box[mh][my][mx] == 0:
                queue.append([mh, my, mx])
                is_visited[mh][my][mx] = True
                box[mh][my][mx] = box[cur[0]][cur[1]][cur[2]] + 1


def find_max() -> int:
    max_cnt = 0
    for i in range(h):
        for j in range(r):
            for k in range(c):
                if 0 < box[i][j][k] > max_cnt:
                    max_cnt = box[i][j][k] - 1
                elif box[i][j][k] == 0:
                    return -1

    return max_cnt


bfs()
sys.stdout.write(str(find_max()))

