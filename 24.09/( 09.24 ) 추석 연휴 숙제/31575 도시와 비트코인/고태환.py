N,M=map(int,input().split())
dx,dy=[1,0],[0,1]
Map=[list(map(int,input().split())) for _ in range(M)]
stack=[(0,0)]
flag=False
while stack:
    x,y=stack.pop()
    Map[x][y]=0
    if x==(M-1) and y==(N-1):
        flag=True
        break
    for i in range(2):
        new_x, new_y = x+dx[i], y+dy[i]
        if 0<=new_x<M and 0<=new_y<N and Map[new_x][new_y]==1:
            stack.append((new_x,new_y))
if flag:
    print('Yes')
else:
    print('No')