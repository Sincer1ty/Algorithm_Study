# 가다가 빙산 만나면 bfs로 다 칠해버리는데
# 마저 순회하다가 빙산 덩어리 수가 2개 되면 날짜 출력
# 순회 다 끝냈으면 빙산 녹이기
from collections import deque
N,M=map(int,input().split())
arctic=[list(map(int,input().split())) for _ in range(N)]
icebergs=deque()
for i in range(N):
    for j in range(M):
        if arctic[i][j] > 0:
            icebergs.append((i,j))
year = 0
dx, dy = [1,-1,0,0], [0,0,1,-1]
melting=[]
while 1:
    visited=[[False for _ in range(M)] for _ in range(N)]
    ice_cnt=0
    is_there_any_ice = False
    ty_ice = len(icebergs)
    # 빙산 순회하다가
    for _ in range(ty_ice):
        x,y = icebergs.popleft()
        # 빙산 만나면 bfs해서 방문 다 때려버리기
        if arctic[x][y] > 0 and not visited[x][y]:
            icebergs.append((x,y))
            is_there_any_ice = True
            ice_cnt+=1
            stack=[(x,y)]
            while stack:
                a,b = stack.pop()
                visited[a][b] = True
                # 빙산 있고 방문 안했으면 방문때리기. 녹일 정보도 기록해두기.
                melt=0
                for k in range(4):
                    i,j = a+dx[k], b+dy[k]
                    if 0<=i<N and 0<=j<M:
                        if arctic[i][j] > 0 and not visited[i][j]:
                            visited[i][j] = True
                            stack.append((i,j))
                        if arctic[i][j] <= 0:
                            melt+=1
                melting.append((a,b,melt))
        elif arctic[x][y] > 0:
            icebergs.append((x,y))

    if not is_there_any_ice:
        year=0
        break

    if ice_cnt > 1:
        break
    year+=1
            
    # 빙산 녹이기
    while melting:
        i,j,melt=melting.pop()
        arctic[i][j]-=melt

print(year)