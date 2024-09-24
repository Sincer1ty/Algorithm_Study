import sys
read = sys.stdin.readline

n,m = map(int, read().split())

graph = []

for i in range(m):
    line = list(map(int,read().split()))
    graph.append(line)

reach = False

# 행
dy = [1,0,-1,0]

# 열
dx = [0,1,0,-1]


def dfs(y,x):
    global reach
    # graph가 0을 도달했을 때 DFS함수가 실행되지 않도록 한다.
    if graph[y][x]==0:
        return

    # graph가 1일 때 0으로 표시하고, DFS 함수를 실행한다.
    if graph[y][x]==1:
        graph[y][x] = 0
    
    # DFS 함수가 마지막 목적지까지 도달한다면, reach = True 로 바꾸고 DFS 함수의 실행을 멈춘다. 
    if y == m-1 and x == n-1 :
        reach = True
        return 
    
    # graph 가 1일 때 갈 수 있는 주변의 선택지를 순회하고, 그 중에서 하나라도 마지막 목적지까지 도달한다면 reach = True를 출력할 것이다.
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        
        if 0 <= ny < m and 0<= nx < n:
            dfs(ny,nx)

    return reach

# # i 행, j 열이므로,
# # m, n 순서를 바꿔서 반복문을 도는 것이 맞다.
# for i in range(m):
#     for j in range(n):
#         if graph[i][j] == 1:
#             dfs(i,j)

# 목적지까지 도달하는 하나의 길이 있는지를 확인하는 함수이기 때문에, For문을 이용할 필요 없이 그냥 시작점만 제공해서 목적지까지 가는지를 확인하면 된다.
dfs(0,0)
if reach:
    print("Yes")
else:
    print("No")


