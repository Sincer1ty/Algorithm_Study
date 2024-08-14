import sys
input = sys.stdin.readline

import heapq

minq = [10001]
maxq = [0]

N = int(input())
for i in range(N):
    num = int(input())
    
    heapq.heappush(maxq, -num)
    
    if minq[0] < maxq[0]*-1:
        min = heapq.heappop(maxq) * -1
        max = heapq.heappop(minq)
        heapq.heappush(minq, min)
        heapq.heappush(maxq, max * -1)
        
    if len(minq) + 1 < len(maxq):
        heapq.heappush(minq, heapq.heappop(maxq) * -1)

    print(maxq[0]*-1)