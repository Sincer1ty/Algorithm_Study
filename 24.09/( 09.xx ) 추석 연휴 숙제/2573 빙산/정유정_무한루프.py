import sys
import copy
from collections import deque

row, col = map(int, sys.stdin.readline().strip().split())
iceberg_org = [[] for _ in range(row)]
for i in range(row):
    iceberg_org[i] = list(map(int, sys.stdin.read().strip().split()))

iceberg_cur = copy.deepcopy(iceberg_org)
is_visited = [[False for _ in range(col)] for _ in range(row)]
years_cnt = 0
queue = deque()


def dfs(cur_y, cur_x):
    if not is_visited[cur_y][cur_x] and iceberg_org[cur_y][cur_x] > 0:
        is_visited[cur_y][cur_x] = True

        for i in range(1, row - 1):
            for j in range(1, col - 1):
                if not is_visited[i][j] and iceberg_org[cur_y][cur_x] > 0:
                    dfs(i, j)


while True:
    flag = False
    for i in range(row):
        for j in range(col):
            if iceberg_org[i][j] <= 0:
                is_visited[i][j] = True
    #         else:
    #             queue.append((i, j))
    #            is_visited[i][j] = True

    for i in range(1, row - 1):
        for j in range(1, col - 1):
            if iceberg_org[i][j] > 0:
                queue.append((i, j))
                is_visited[i][j] = True
                flag = True
                break
        if flag:
            flag = False
            break
    years_cnt += 1

# BFS로 1년 뒤 빙산 크기 표시
    while queue:
        cur_y, cur_x = queue.popleft()
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        decrease = 0

        for i in range(4):
            my, mx = dy[i] + cur_y, dx[i] + cur_x
            if not is_visited[my][mx] and 0 <= mx < col and 0 <= my < row and iceberg_org[my][mx] > 0:
                queue.append((my, mx))
                is_visited[my][mx] = True

            elif iceberg_org[my][mx] <= 0:
                decrease += 1

        iceberg_cur[cur_y][cur_x] -= decrease

    is_visited = [[False for _ in range(col)] for _ in range(row)]
    iceberg_org = copy.deepcopy(iceberg_cur)

    for i in range(1, row - 1):
        for j in range(1, col - 1):
            if iceberg_org[i][j] > 0:
                dfs(i, j)
                flag = True
                break
        if flag:
            break

    if any(False in r for r in is_visited):
        print(years_cnt)
        break
    elif all(num <= 0 for r in iceberg_org for num in r):
        print(0)
        break

    # if any(False in r for r in is_visited):
    #     print(years_cnt)
    #     break
    # else:
    #     if all(num <= 0 for r in iceberg_org for num in r):
    #         print(0)
    #         break
    #
    # is_visited = [[False for _ in range(col)] for _ in range(row)]
    # iceberg_org = copy.deepcopy(iceberg_cur)

