import sys
sys.setrecursionlimit(10**5)
# 해당 도시까지 걸리는 최대 시간 경로 갱신
def max_time(city):
    if city==start:
        return 0
    if time[city]==-1: # 아직 탐색하지 않았다면
        for s,t in graph[city]:
            bef_time = max_time(s)+t
            if time[city] < bef_time: # 최대 경로가 갱신됐다면
                time[city] = bef_time
                course[city] = [s]
            elif time[city] == bef_time: # 최대 경로를 더 발견했다면
                time[city] = bef_time
                course[city].append(s)
    return time[city]

import sys
input = sys.stdin.readline
n=int(input()) # 도시의 개수
m=int(input()) # 도로의 개수
time=[-1]*(n+1) # 도시 도착 최대 시간
course=[[] for _ in range(n+1)]
graph=[[] for _ in range(n+1)] # 각 도시로 향하는 경로
# 도로 정보 받기
for _ in range(m):
    s,a,t = map(int,input().split())
    graph[a].append((s,t))
start,arrive=map(int,input().split())

print(max_time(arrive))
from collections import deque
result=set()
q=deque()
q.append(arrive)
while q:
    city=q.popleft()
    for bef in course[city]:
        if (bef,city) not in result:
            result.add((bef,city))
            q.append(bef)
print(len(result))


