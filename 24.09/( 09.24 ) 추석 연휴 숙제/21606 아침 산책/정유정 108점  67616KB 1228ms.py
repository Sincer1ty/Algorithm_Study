import sys

node = int(sys.stdin.readline().strip())
location_type = list(map(int, sys.stdin.readline().strip()))
location_type.insert(0, -1)
school_map = [[] for _ in range(node + 1)]
is_visited = [False] * (node + 1)
is_visited[0] = True
cnt = 0

for i in range(node - 1):
    x, y = map(int, sys.stdin.readline().strip().split())
    school_map[x].append(y)
    school_map[y].append(x)


def dfs(idx, depth):
    global cnt

    if depth != 1 and (location_type[idx] == 1 or all(is_visited)):
        if location_type[idx] == 1:
            cnt += 1
        return

    for i in range(len(school_map[idx])):
        check = school_map[idx][i]
        # print(f"check value: {check}, type: {type(check)}")
        if is_visited[check]:
            continue

        if location_type[check] == 0:
            is_visited[check] = True
            dfs(check, depth + 1)
            is_visited[check] = False

        elif location_type[check] == 1:
            cnt += 1
            continue
    return



for i in range(1, node + 1):
    if location_type[i] == 1 and not is_visited[i]:
        is_visited[i] = True
        dfs(i, 1)
        is_visited[i] = False
print(cnt)
