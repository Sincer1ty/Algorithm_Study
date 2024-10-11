import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(input()) # 도로의 개수
W = int(input()) # 사건의 개수
cases = [(1,1),(N,N)]
for _ in range(W):
    ew, ns = map(int,input().split())
    cases.append((ew,ns))
dp = [[-1]*(W+2) for _ in range(W+2)]
course = [[-1]*(W+2) for _ in range(W+2)]
# 규칙이 없는 경로들의 비용 최솟값이므로 모든 경로의 비용 중 최소를 구해야 함
# 모든 경로를 계산하려면 2의 n승. 불가능하므로 dp 사용.
# 필요한 정보 : (왼쪽 혹은 오른쪽에서) 경로가 정해진다면, 나머지 경로에서의 최소 경로 비용
# dp로 경로 계산을 생략하려면 공통되는 부분이 필요한데,
# 경찰차당 마지막으로 출동했던 사건의 번호를 인덱스로 설정하면 됨
# 자연스럽게 왼쪽에서 경로를 정한 다음 오른쪽의 정보를 요구하는 재귀가 됨.
def distance(a,b):
    return abs(cases[a][0]-cases[b][0])+abs(cases[a][1]-cases[b][1])

def min_d(a,b):
    next = max(a,b)+1
    if next == W+2:
        return 0
    if dp[a][b] != -1:
        return dp[a][b]    
    a_cost = min_d(next,b)+distance(a,next)
    b_cost = min_d(a,next)+distance(b,next)
    if a_cost < b_cost: 
        course[a][b] = 1
        dp[a][b] = a_cost
    else: 
        course[a][b] = 2
        dp[a][b] = b_cost
    return dp[a][b]

min_d(0,1) # 첫번째 경찰차는 1,1, 두번째 경찰차는 N,N에서 시작
print(dp[0][1])

a,b,cnt=0,1,2
while cnt < W+2:
    car = course[a][b]
    print(car)
    if car == 1: a=cnt
    else: b=cnt
    cnt+=1
