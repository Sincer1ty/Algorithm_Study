import sys
input=sys.stdin.readline
N=int(input())
arr=list(map(int,input().split()))

dp=list([0]*N for _ in range(N))

for length in range(1,N): #부분 배열의 길이
    for s in range(N-length): #시작 인덱스
        e=s+length #끝 인덱스
        if arr[s]==arr[e]:
            dp[s][e]=dp[s+1][e-1]
        else:
            dp[s][e]=min(dp[s+1][e],dp[s][e-1])+1

print(dp[0][N-1])
