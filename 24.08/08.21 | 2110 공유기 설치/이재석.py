import sys
read = sys.stdin.readline

n, rout_n = map(int,read().strip().split())

loc = []
for i in range(n):
    x = int(read().strip())
    loc.append(x)
loc.sort()

# min, max 변수는 모두 가장 인접한 공유기 간 거리를 나타내기 위한 변수
min = 1
max = loc[-1] - loc[0]
ans = 0

# 이진 탐색이 마무리될 때 까지, 공유기 간 거리가 가장 인접한 공유기 간 거리보다 클 때 공유기를 설치
# 공유기의 개수가 너무 많다면 공유기 간 거리를 늘려서 개수를 줄이고, 공유기의 개수가 너무 적다면 공유기 간 거리를 줄여서 개수를 늘린다
while min <= max:
    mid = (min+max) // 2
    cur = loc[0]
    cnt = 1
    
    for i in range(1,n):
        if loc[i] - cur >= mid:
            cnt+=1
            cur = loc[i]

    if cnt >= rout_n:
        if ans < mid:
            ans = mid
        min = mid + 1
    else:
        max = mid - 1

print(ans)

        
