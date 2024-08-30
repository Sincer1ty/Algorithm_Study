import sys
from collections import deque

row, col = map(int, sys.stdin.readline().strip().split())
forest_map = []

beaver_home = []
hedgehog_queue = deque()
water_queue = deque()
is_visited = [([False] * col) for _ in range(row)]

for r in range(row):
    insert_map = (list(map(str, list(sys.stdin.readline().strip()))))
    if 'D' in insert_map:
        beaver_home = r, insert_map.index('D')

    if 'S' in insert_map:
        s_location = (r, insert_map.index('S'))
        hedgehog_queue.extend(s_location)
        is_visited[s_location[0]][s_location[1]] = True

    if '*' in insert_map:
        water_queue.extend((r, insert_map.index('*')))

time_check = -1
is_arrive = False
while hedgehog_queue:
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    mx, my = 0, 0

    if water_queue:
        cur_water = water_queue.popleft()

        if cur_water == beaver_home:
            is_arrive = True
            break

        for i in range(4):
            mx = cur_water[1] + dx[i]
            my = cur_water[0] + dy[i]

            if mx >= col or mx < 0 or my >= row or my < 0:
                continue

            if forest_map[my][mx] == '.':
                water_queue.extend((my, mx))

    cur_hedgehog = hedgehog_queue.popleft()
    time_check += 1

    for i in range(4):
        mx = cur_hedgehog[1] + dx[i]
        my = cur_hedgehog[0] + dy[i]

        if mx >= col or mx < 0 or my >= row or my < 0:
            continue

        if not is_visited[my][mx] and not [my, mx] in water_queue and forest_map[my][mx] != 'X':
            hedgehog_queue.extend((my, mx))
            is_visited[my][mx] = True

if is_arrive:
    sys.stdout.write(str(time_check))
else:
    sys.stdout.write("KAKTUS")
