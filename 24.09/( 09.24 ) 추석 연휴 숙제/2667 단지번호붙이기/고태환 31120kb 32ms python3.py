N=int(input())
Map = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    str = input()
    for j in range(N):
        Map[i][j] = int(str[j])
dx, dy = [1,-1,0,0], [0,0,1,-1]
apts=[]
for i in range(N):
    for j in range(N):
        if Map[i][j] == 1:
            apt = 0
            stack=[(i,j)]
            # dfs 돌려서 아파트 칠해버리기
            while stack:
                x,y=stack.pop()
                if Map[x][y]==1:
                    Map[x][y]=0
                    apt+=1
                    for k in range(4):
                        if 0<=x+dx[k]<N and 0<=y+dy[k]<N:
                            if Map[x+dx[k]][y+dy[k]] == 1:
                                stack.append((x+dx[k],y+dy[k]))
            apts.append(apt)
print(len(apts))
apts.sort()
for apt in apts:
    print(apt)