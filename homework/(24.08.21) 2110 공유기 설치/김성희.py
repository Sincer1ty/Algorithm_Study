import sys
input = sys.stdin.readline

# 집 N개, 공유기 C개
N, C = map(int, input().split())

home = []
for _ in range(N):
    home.append(int(input()))

home.sort()

# 한 집에는 공유기 하나
# 인접한 두 공유기 사이의 거리 최대
dist = home[-1] - home[0]

# 인덱스 반환
def bSearch(pl, pr, find):
    while pr - 1 != pl:
        idx = (pl + pr) // 2

        if home[idx] > find:
            pr = idx
        else : 
            pl = idx
    before = find - home[pl]
    after = home[pr] - find
    return pl if before < after else pr

C -= 2
pl = 0
result = []
while C != 0:
    cut = dist // (C+1)
    temp = pl
    pl = bSearch(pl, N-1, home[pl] + cut)
    dist = home[-1] - home[pl]
    result.append(home[pl] - home[temp])
    C -= 1

result.append(home[-1] - home[pl])

print(min(result))