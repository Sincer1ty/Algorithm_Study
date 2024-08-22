from collections import deque
import sys
input=sys.stdin.readline
N=int(input())
area = [list(map(int,input().split())) for _ in range(N)]
# print(area)
# arr_min = min(min(row) for row in area)
# arr_max = max(max(row) for row in area)
arr_min=0
arr_max=0
# 최댓값 최솟값 찾기(이중포문)
for i in range(N):
    for j in range(N):
        if i>0 and j> 0:
            if area[i][j]>arr_max:
                arr_max = area[i][j]
            if area[i][j]<arr_min:
                arr_min = area[i][j]
# 상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def search_safezone(num):
    count=0
    visited=[[False]*(N) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if num<area[i][j] and visited[i][j]==False:
                queue=deque([(i,j)])
                visited[i][j]=True
                while queue:
                    x,y=queue.popleft()
                    for k in range(4):
                        nx,ny=x+dx[k],y+dy[k]
                        if 0<= nx <N and 0<= ny < N and area[nx][ny]>num and visited[nx][ny]==False:
                            queue.append((nx,ny))
                            visited[nx][ny]=True
                count+=1
    return count
safezone_count=[]
# 비 안올때라는데 최대개수 구하는데서는 필요없는듯 그 이외에서는 안전영역 개수가 1일것이기 때문에
# safezone_count.append(search_safezone(0))
# 최솟값부터 최댓값 전까지 탐색
for i in range(arr_min,arr_max):
    num=search_safezone(i)
    safezone_count.append(num)

print(max(safezone_count))
