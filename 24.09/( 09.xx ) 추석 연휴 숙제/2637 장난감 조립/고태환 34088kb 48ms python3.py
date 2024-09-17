import sys
input = sys.stdin.readline
from collections import deque
N=int(input()) # 1~N-1은 부품, N은 완제품
M=int(input()) # edge 개수
bp=[[] for _ in range(N+1)] # 해당 부품이 쓰이는 중간 부품/완제품
res=[[0 for _ in range(N+1)] for _ in range(N+1)] # 중간 부품/완제품이 필요로 하는 기본 부품들
indegree=[0 for _ in range(N+1)] # 진입차수
queue = deque() # 기본 부품부터 시작해서 중간 부품들을 전부 기본 부품들의 조합으로 바꾼다
basic=[]
# 부품 조합법을 받는다
for _ in range(M):
    X,Y,K=map(int,input().split()) # X 만들 때 Y가 K개 필요하다
    bp[Y].append((X,K)) # Y가 X에 K개 필요하다
    indegree[X]+=1
# 기본 부품 리스트 세기
for i in range(1,N):
    if indegree[i]==0:
        basic.append(i)
# 기본 부품들로부터 시작
for i in basic:
    for p in bp[i]:
        X,Y,K=p[0],i,p[1]
        res[X][Y]=K
        indegree[X]-=1
        if indegree[X]==0:
            queue.append(X)
# 부품들 조립해서 만들기
while queue:
    Y = queue.popleft()
    for X,K in bp[Y]: # Y가 쓰이는 중간 부품들에 대해
        for i in basic:
            res[X][i]+=res[Y][i]*K
        indegree[X]-=1
        if indegree[X]==0:
            queue.append(X)
# 완제품에 쓰이는 기본 부품 출력
for i in basic:
    print(i,res[N][i])