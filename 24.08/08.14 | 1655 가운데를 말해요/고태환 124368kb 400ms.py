import heapq
import sys
input = sys.stdin.readline

N = int(input())
max_h = []  # 최대 힙 (파이썬 힙은 최소 힙이므로, 음수 값을 넣어 최대 힙처럼 사용)
min_h = []  # 최소 힙

for i in range(N):
    n = int(input())
    
    if len(max_h) == len(min_h):
        heapq.heappush(max_h, -n)
    else:
        heapq.heappush(min_h, n)
    
    if min_h and -max_h[0] > min_h[0]:
        max_val = -heapq.heappop(max_h)
        min_val = heapq.heappop(min_h)
        heapq.heappush(max_h, -min_val)
        heapq.heappush(min_h, max_val)
    
    print(-max_h[0])
