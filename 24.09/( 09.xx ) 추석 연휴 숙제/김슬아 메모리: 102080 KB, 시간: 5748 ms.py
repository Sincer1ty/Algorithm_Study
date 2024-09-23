# 200점 답 : 클로드 도움
import sys
sys.setrecursionlimit(10**6)
# 정점의 수
N=int(input()) 
# 실내 실외 정보
A=input()
graph=[[]for _ in range(N+1)]

indoor=set()
for i in range(1,N+1):
    if A[i-1]=="1":
        indoor.add(i)
for _ in range(N-1):
    a,b = map(int,input().strip().split())
    graph[a].append(b)
    graph[b].append(a)

count=0
# 1. 실내 노드끼리 직접 연결된 경우 카운트
for i in indoor:
    for neighbor in graph[i]:
        if neighbor in indoor:
                count+=1

visited=[False]*(N+1)

def dfs(s):
    visited[s]=True
    cnt=0
    for neighbor in graph[s]:
        if not visited[neighbor]:
            if neighbor in indoor:
                cnt+=1
            else:
                cnt+=dfs(neighbor)
    return cnt

for i in range(1,N+1):
    if i not in indoor and not visited[i]:
        num = dfs(i)
        count +=num*(num-1)

print(count)

# 73점 답
import sys
sys.setrecursionlimit(10**6)
N=int(input())
A=input()
graph=[[]for _ in range(N+1)]
indoor=[]
for _ in range(N-1):
    a,b = map(int,input().strip().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1,len(A)+1):
    if A[i-1]=="1":
        indoor.append(i)
count=0
def dfs(s):
    global count
    visited[s]=True
    for neighbor in graph[s]:
        if not visited[neighbor]:
            if neighbor in indoor:
                count+=1
            else:
                dfs(neighbor)
for i in range(len(indoor)):
    visited=[False]*(N+1)
    dfs(indoor[i])
print(count)
