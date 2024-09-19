import sys
from collections import deque

map_size = int(sys.stdin.readline().strip())
apt_map = [[] for _ in range(map_size)]
for i in range(map_size):
    apt_map[i] = list(map(int, sys.stdin.readline().strip()))
is_visited = [[False for _ in range(map_size)]for _ in range(map_size)]
queue = deque()
total_cnts = 0
house_cnts = []

for i in range(map_size):
    for j in range(map_size):
        if apt_map[i][j] == 0 or is_visited[i][j]:
            continue
        house_cnt = 0
        queue.append((i, j))
        is_visited[i][j] = True
        house_cnt += 1

        while queue:
            cur_y, cur_x = queue.popleft()
            dx = [0, 0, -1, 1]
            dy = [-1, 1, 0, 0]

            for k in range(4):
                move_y = cur_y + dy[k]
                move_x = cur_x + dx[k]
                if move_x < 0 or move_x >= map_size or 0 > move_y or move_y >= map_size:
                    continue

                if apt_map[move_y][move_x] == 1 and not is_visited[move_y][move_x]:
                    queue.append((move_y, move_x))
                    is_visited[move_y][move_x] = True
                    house_cnt += 1

        house_cnts.append(house_cnt)
        total_cnts += 1

house_cnts.sort()

print(total_cnts)
for house in house_cnts:
    print(house)
