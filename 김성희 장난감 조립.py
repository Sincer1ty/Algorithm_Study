import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

part = [[] for _ in range(N)]
count = [0] * N
for _ in range(M):
    X, Y, K = map(int, input().split())
    part[X - 1].append((Y, K))

for i, p in enumerate(part):
    if len(p):
        basic = i
        break

def dfs(n, many):
    for p, c in part[n]:
        if p <= basic:
            count[p - 1] += c * many
        else:
            dfs(p - 1, c * many)

dfs(N - 1, 1)

for i, c in enumerate(count):
    if i == basic:
        break
    print(i + 1, c)
