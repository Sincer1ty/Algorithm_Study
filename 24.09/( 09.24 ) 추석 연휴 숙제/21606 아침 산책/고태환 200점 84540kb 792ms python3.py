import sys
input = sys.stdin.readline
N=int(input())
IO=[-1]+list(input().strip()) # 안인지 밖인지
visited = [False for i in range(N+1)] # 방문을 했었는지
course = 0
graph={i:[] for i in range(N+1)}
for _ in range(N-1): # 간선 받기
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

# 순회하다가 밖이고 visited=false면 탐색 시작
# 안이 발견되면 안 개수 더하고 더 탐색 x
# 탐색 다 끝내면 안 개수가 n이라고 할 때 n(n-1)

for i in range(1,N+1):
    if IO[i]=='0' and visited[i]==False: # 탐색의 시작점
        visited[i] = True # 여기 == 해놓고 왜 안되지? 이러고 있었음
        stack=[i]
        in_cnt = 0
        while stack:
            e = stack.pop()
            for edge in graph[e]:
                if IO[edge]=='1': 
                    in_cnt+=1
                elif IO[edge]=='0' and visited[edge]==False: 
                    visited[edge]=True
                    stack.append(edge)
        course += in_cnt*(in_cnt-1)

    # 순회하다가 안이면 탐색 시작
    # 자기가 갖고 있는 간선들 확인하고 안이면 경로 개수 더하기
    elif IO[i]=='1':
        for edge in graph[i]:
            if IO[edge]=='1':
                course+=1

print(course)
