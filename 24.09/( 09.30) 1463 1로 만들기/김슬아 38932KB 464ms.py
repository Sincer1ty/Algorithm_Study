# 내가 처음에 푼 코드
import sys
N=int(input())
input= sys.stdin.readline
dp=[float("inf")]*(N+1)
for i in range(1,N+1):
    if i == 1 : 
        dp[i]=0
    elif i%2 ==0 and i%3 ==0:
        dp[i]=min(1+dp[i//2],1+dp[i//3])
    elif i%2 ==0:
        dp[i]=min(1+dp[i//2],dp[i-1]+1)
    elif i%3 ==0:
        dp[i]=min(1+dp[i//3],dp[i-1]+1)
    else:
        dp[i] = dp[i-1]+1

print(dp[N])
# 클로드가 내꺼 최적화 해 준 코드
import sys
N=int(input())
input= sys.stdin.readline
dp=[0]*(N+1)
for i in range(1,N+1):
    if i == 1 : 
        dp[i]=0
    elif i%2 ==0 and i%3 ==0:
        dp[i]=min(dp[i//2],dp[i//3])+1
    elif i%2 ==0:
        dp[i]=min(dp[i//2],dp[i-1])+1
    elif i%3 ==0:
        dp[i]=min(+dp[i//3],dp[i-1])+1
    else:
        dp[i] = dp[i-1]+1

print(dp[N])
# 클로드가 최적화 해준 코드인데 내꺼보다 더 느림
import sys
N=int(input())
input= sys.stdin.readline
dp=[0]*(N+1)
for i in range(2,N+1):
    dp[i] = dp[i-1]+1
    if i%2 ==0:
        dp[i]=min(1+dp[i//2],dp[i])
    if i%3 ==0:
        dp[i]=min(1+dp[i//3],dp[i])
        
print(dp[N])
