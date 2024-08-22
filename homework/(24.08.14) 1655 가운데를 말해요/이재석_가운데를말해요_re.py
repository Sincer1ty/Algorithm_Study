import sys
import heapq

read = sys.stdin.readline
left_heap = []
right_heap = []

n = int(read().strip())

'''
for i in range(n):
    ele = int(read().strip())
    heapq.heappush(left_heap, -ele)
    
    if len(left_heap) != len(right_heap):
        heapq.heappush(right_heap,ele)
        if left_heap[-1] > right_heap[0]:
            right_heap[0], left_heap[-1] = left_heap[-1], right_heap[0]

for i in range(n):
    ele = int(read().strip())
    
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -ele)
    
    else:
        heapq.heappush(right_heap,ele)
        if left_heap[-1] > right_heap[0]:
            right_heap[0], left_heap[-1] = left_heap[-1], right_heap[0]
'''

for i in range(n):
    ele = int(read().strip())
    
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -ele)
    else:
        heapq.heappush(right_heap, ele)

        if -left_heap[0] > right_heap[0]:
            right_heap[0], left_heap[0] = left_heap[0], right_heap[0]


    print(-left_heap[0])

    
