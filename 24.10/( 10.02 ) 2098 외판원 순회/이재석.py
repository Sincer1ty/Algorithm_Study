import sys
read = sys.stdin.readline

graph = []
n = int(read().strip())

for i in range(n):
    line = list(map(int,read().strip().split()))
    graph.append(line)


INF = int(10**9)
dp = [[INF] * (1<<n) for i in range(n)]

def dfs(x, visited):
    if visited == (1<<n) -1:
        if graph[x][0]:
            return graph[x][0]
        else:
            return INF
    
    if dp[x][visited] != INF:
        return dp[x][visited]
    
    for i in range(1,n):
        if not graph[x][i]:
            continue
        if visited & (1<<i):
            continue

        dp[x][visited] = min(dp[x][visited], dfs(i,visited|(1<<i)) + graph[x][i] )    

    return dp[x][visited]


print(dfs(0,1))
