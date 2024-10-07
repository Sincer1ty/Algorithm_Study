import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**8)

N = int(input())

numbers = list(map(int, input().split()))

dp = [[0] * N for _ in range(N)]
def check(pl, pr):
    if pl >= pr:
        return
    
    if numbers[pl]  == numbers[pr]:
        check(pl+1, pr-1)
        return
    
    # if i == -1:
    #     dp[0] += 1
    #     check(pl+1, pr, 0)
    #     dp[1] += 1
    #     check(pl, pr-1, 1)
    #     return
    
    dp[pl][pr] += 1
    # if i == 0:
    check(pl+1, pr)
    # elif i == 1:
    check(pl, pr-1)

check(0, N-1)
print(dp)