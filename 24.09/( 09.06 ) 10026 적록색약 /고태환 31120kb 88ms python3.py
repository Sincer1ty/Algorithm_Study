N=int(input())
L = [list(input()) for _ in range(N)] # 이거 받는 법 또 까먹었었음
L2 = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if L[i][j] == 'R' or L[i][j] == 'G':
            L2[i][j] = 'R'
        else:
            L2[i][j] = 'B'


# 정상인
cnt = 0
dx, dy = [1,-1,0,0], [0,0,1,-1]
for i in range(N):
    for j in range(N):
        if L[i][j] != -1:
            a = L[i][j]
            stack=[(i,j)]
            cnt += 1
            while stack:
                x, y = stack.pop()
                # a = L[x][y] 여기에 넣었더니 -1이 무한반복. 이미 -1로 변한 놈이 스택에서 나올 수 있음.
                L[x][y] = -1
                for k in range(4):
                    if  (0<= x+dx[k] < N) and (0<= y+dy[k] < N):
                        if L[x+dx[k]][y+dy[k]] == a:
                            stack.append((x+dx[k],y+dy[k]))
# 적록색약
cnt2 = 0
for i in range(N):
    for j in range(N):
        if L2[i][j] != -1:
            a = L2[i][j]
            stack=[(i,j)]
            cnt2 += 1
            while stack:
                x, y = stack.pop()
                L2[x][y] = -1
                for k in range(4):
                    if  (0<= x+dx[k] < N) and (0<= y+dy[k] < N):
                        if L2[x+dx[k]][y+dy[k]] == a: # 여기 L2로 안 바꿔줌
                            stack.append((x+dx[k],y+dy[k]))

print(cnt, cnt2)

# 어려움 : 적록 색약인 놈이 보는 것도 추가해야 함
