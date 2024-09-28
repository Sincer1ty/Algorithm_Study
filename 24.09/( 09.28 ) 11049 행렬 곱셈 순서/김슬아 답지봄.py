import sys
input = sys.stdin.readline
N=int(input())
matrix =[list(map(int, input().split())) for _ in range(N)]
dp=[[float('inf')]*N for _ in range(N)]

for i in range(N):
    dp[i][i]=0
for num in range(1,N):
    for i in range(N-num):
        j=i+num
        for k in range(i, j):
            dp[i][j] = min(dp[i][j],  dp[i][k] + dp[k+1][j] + matrix[i][0] * matrix[k][1] * matrix[j][1])
print(dp[0][N-1])
