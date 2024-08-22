import sys

read =sys.stdin.readline

n, rout_n = map(int,read().strip().split())

hs_list = []
for i in range(n):
    loc = int(read().strip())
    hs_list.append(loc)

hs_list.sort()

# 집 간의 거리를 변수로 잡아서, 이진 탐색을 하는 것이 문제의 핵심
start = 1
end = hs_list[-1] - hs_list[0]
answer = 0

while start <= end:    
    #첫번째 집에서부터 공유기를 설치해야, 가장 인접한 공유기 간 거리를 최대로 만들 수 있어  
    cur = hs_list[0]
    cnt = 1

    mid = (start + end) // 2
    
    for i in range(1, n):
        if hs_list[i] - cur >= mid:
            cnt+=1
            cur = hs_list[i]

    if cnt < rout_n:
        end = mid -1
    else:
        if answer < mid:
            answer = mid
        start = mid +1

print(answer)

