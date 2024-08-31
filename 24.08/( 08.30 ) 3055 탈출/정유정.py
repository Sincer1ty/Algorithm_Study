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
    forest_map.append(insert_map)
    if 'D' in insert_map:
        beaver_home = [r, insert_map.index('D')]

    if 'S' in insert_map:
        s_location = [r, insert_map.index('S')]
        hedgehog_queue.append(s_location)
        is_visited[s_location[0]][s_location[1]] = True
        forest_map[s_location[0]][s_location[1]] = '.'
        hedgehog_queue.append(0)

    if '*' in insert_map:
        water_queue.append([r, insert_map.index('*')])

water_queue.append(0)
time_check = 0
is_arrive = False

while hedgehog_queue != deque([0]):
    if beaver_home in hedgehog_queue:
        is_arrive = True
        break

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    mx, my = 0, 0

    if water_queue:
        cur_water = water_queue.popleft()
        for _ in range(len(water_queue)):
            for i in range(4):
                mx = cur_water[1] + dx[i]
                my = cur_water[0] + dy[i]

                if mx >= col or mx < 0 or my >= row or my < 0:
                    continue

                if forest_map[my][mx] == '.' and [my, mx] not in water_queue:
                    water_queue.append([my, mx])
                    forest_map[my][mx] = '*'
                    # is_visited[my][mx] = True
            water_queue.append(cur_water)
            cur_water = water_queue.popleft()

    water_queue.append(0)
    cur_hedgehog = hedgehog_queue.popleft()
    for _ in range(len(hedgehog_queue)):
        for i in range(4):
            mx = cur_hedgehog[1] + dx[i]
            my = cur_hedgehog[0] + dy[i]

            if mx >= col or mx < 0 or my >= row or my < 0:
                continue

            if not is_visited[my][mx] and (forest_map[my][mx] == '.' or forest_map[my][mx] == 'D'):
                hedgehog_queue.append([my, mx])
                is_visited[my][mx] = True
        cur_hedgehog = hedgehog_queue.popleft()

    hedgehog_queue.append(0)
    time_check += 1

if is_arrive:
    sys.stdout.write(str(time_check))
else:
    sys.stdout.write("KAKTUS")
