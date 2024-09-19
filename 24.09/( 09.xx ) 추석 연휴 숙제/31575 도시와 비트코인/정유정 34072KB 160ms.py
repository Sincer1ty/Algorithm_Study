import sys
from collections import deque

col, row = map(int, sys.stdin.readline().strip().split())
if col == row and col == 1:
    sys.stdin.readline()
    print('Yes')
else:
    city_map = [[] for _ in range(row)]
    for i in range(row):
        city_map[i] = list(map(int, sys.stdin.readline().strip().split()))
    is_visited = [[False for _ in range(col)] for _ in range(row)]
    queue = deque()
    queue.append((0, 0))
    is_visited[0][0] = True
    while queue:
        cur_y, cur_x = queue.popleft()
        dx = [0, 1]
        dy = [1, 0]

        for i in range(2):
            move_x = cur_x + dx[i]
            move_y = cur_y + dy[i]

            if (move_x < 0 or col <= move_x or move_y < 0 or row <= move_y
                    or is_visited[move_y][move_x] or city_map[move_y][move_x] == 0):
                continue
            queue.append((move_y, move_x))
            is_visited[move_y][move_x] = True

    if is_visited[row - 1][col - 1]:
        print('Yes')
    else:
        print('No')


