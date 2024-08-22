#완전히 다 보고 함
#우선순위 큐, 힙에 대한 정리 다시 필요
#우선순위 큐라는 추상적인 데이터 구조를, 힙을 통해서 구현

import heapq
import sys

read = sys.stdin.readline

left_heap = []
right_heap = []

n = int(read().strip())

for i in range(n):
    num = int(read().strip())

    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -num)
    else:
        heapq.heappush(right_heap, num)

    if right_heap and right_heap[0]<-left_heap[0]:
        leftval = heapq.heappop(left_heap)
        rightval = heapq.heappop(right_heap)

        heapq.heappush(left_heap, -rightval)
        heapq.heappush(right_heap, -leftval)
    
    print(-left_heap[0])