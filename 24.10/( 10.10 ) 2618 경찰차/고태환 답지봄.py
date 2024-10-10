import sys
input = sys.stdin.readline

def DFS(p1,p2):
  next = max(p1,p2)+1
  if next == W+2:
    return
  if not DP[next][p2]:
    DFS(next,p2)
  if not DP[p1][next]:
    DFS(p1,next)  
  x1,x2 = DP[next][p2]+graph[p1][next],DP[p1][next]+graph[p2][next]
  if x1<x2:
    DP[p1][p2],path[p1][p2] = x1,1
  else:
    DP[p1][p2],path[p1][p2] = x2,2

N,W = int(input()),int(input())

case = [[1,1],[N,N]]+[[*map(int,input().split())] for i in range(W)]
graph = [[0]*(W+2) for i in range(W+2)]
for i in range(W+1):
  for j in range(i+1,W+2):
    graph[i][j] = abs(case[i][0]-case[j][0])+abs(case[i][1]-case[j][1])

DP,path = [[0]*(W+2) for i in range(W+2)],[[0]*(W+2) for i in range(W+2)]
DFS(0,1)
print(DP[0][1])
p1,p2 = 0,1
while max(p1,p2)<W+1:
  print(path[p1][p2])
  if path[p1][p2] == 1:
    p1 = max(p1,p2)+1
  else:
    p2 = max(p1,p2)+1