from collections import deque
M,N,H=map(int,input().split())
box=[[] for _ in range(H)]
for i in range(H):
    for j in range(N):
        box[i].append(list(map(int,input().split())))
# 토마토 어디 있는지 탐색
# i : 층수, j : 세로, k : 가로
q = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if (box[i][j][k]==1):
                q.append((i,j,k))
# 큐에 들어있는 size만큼 빼내는거 반복하고 cnt 올리기
# 큐에서 빼내면 6방향 색칠한 뒤 색칠한 부분들 큐에 넣기
# 큐에 더 이상 아무것도 안 들어있으면 종료
di = [1,-1,0,0,0,0]
dj = [0,0,1,-1,0,0]
dk = [0,0,0,0,1,-1]
cnt = -1
while(q):
    cnt+=1
    repeat = len(q)
    for _ in range(repeat):
        i, j, k = q.popleft()
        for n in range(6):
            # 색칠 가능하다면 색칠하고 큐에 넣기
            if 0<=i+di[n]<H and 0<=j+dj[n]<N and 0<=k+dk[n]<M:
                if box[i+di[n]][j+dj[n]][k+dk[n]] == 0:
                    box[i+di[n]][j+dj[n]][k+dk[n]] = 1
                    q.append((i+di[n],j+dj[n],k+dk[n]))
# 다 익었는지 확인
all_ripe = 1
for i in range(H):
    for j in range(N):
        for k in range(M):
            if (box[i][j][k]==0):
                all_ripe = 0

if all_ripe:
    print(cnt)
else:
    print(-1)

# 실수 : i+di[n] 안 하고 box[i][j][k] 해버림
