import sys
input = sys.stdin.readline

def w(a,b,c):
    if a<=0 or b<=0 or c<=0:
        return 1
    elif dp[a][b][c] != None:
        return dp[a][b][c]
    elif a>20 or b>20 or c>20:
        dp[a][b][c] = w(20,20,20)
    elif a<b and b<c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return dp[a][b][c]

dp=[[[None for _ in range(51)]for _ in range(51)] for _ in range(51)]
a,b,c=map(int,input().split())
while (a,b,c) != (-1,-1,-1):
    print('w('+str(a)+', '+str(b)+', '+str(c)+') =',w(a,b,c))
    a,b,c=map(int,input().strip().split())

# a,b,c가 0보다 작거나 같으면 1을 return
# a,b,c가 20 초과이면 w(20,20,20) return
# a<b<c이면 w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c) return
# 전부 다 아니라면 w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)