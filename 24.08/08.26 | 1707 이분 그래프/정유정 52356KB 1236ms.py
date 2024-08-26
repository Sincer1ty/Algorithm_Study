import sys
from collections import deque

test_case = int(sys.stdin.readline())
for _ in range(test_case):
    vertex, edge = map(int, sys.stdin.readline().split())

    graph = [[] for _ in range(vertex + 1)]
    is_visited = [False] * (vertex + 1)
    is_visited[0] = True

    for _ in range(edge):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    color = [0] * (vertex + 1)
    is_binary_graph = True

    for i in range(vertex):
        if is_visited[i]:
            continue

        queue = deque()
        queue.append(i)
        is_visited[i] = True
        color[i] = 1

        while queue:
            check = queue.popleft()

            for val in graph[check]:
                if color[check] == color[val]:
                    is_binary_graph = False
                    break

                if not is_visited[val]:
                    queue.append(val)
                    is_visited[val] = True
                    color[val] = color[check] + 1

    if is_binary_graph:
        sys.stdout.write("YES\n")
    else:
        sys.stdout.write("NO\n")

