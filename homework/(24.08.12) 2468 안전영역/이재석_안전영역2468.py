#1st Try
import sys
read = sys.stdin.readline

n = int(read().strip())

dstrct_tbl = []
sink_tbl = [[False]*n for _ in range(n)]

for i in range(n):
    line = list(map(int, read().strip().split()))
    dstrct_tbl.append(line)

# x, y 지점에 따라 탐색하는 재귀함수 
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def search_dstrct(x,y,h):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        
        if (0<=nx<n) and (0<=ny<n) and not sink_tbl[nx][ny] and dstrct_tbl[nx][ny]>h:
            sink_tbl[nx][ny] = True
            search_dstrct(nx,ny,h)

        
