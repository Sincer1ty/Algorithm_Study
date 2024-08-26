#시간초과나서 본 답
import heapq
import sys

input=sys.stdin.readline
N=int(input())
# print(nums)

left_heap=[]
right_heap=[] 

for i in range(N):
    num=int(input())

    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -num)
    else:
        heapq.heappush(right_heap, num)
    if right_heap and -left_heap[0]>right_heap[0]:
        left_max = -heapq.heappop(left_heap)
        right_min = heapq.heappop(right_heap)
        heapq.heappush(right_heap,left_max)
        heapq.heappush(left_heap,-right_min)
    print(-left_heap[0])

#번갈아서 나와도 되는 거였다니,,

#heapq 사용법만 보고 낸 답
#출력입력 모두 한꺼번에 받고 한꺼번에 출력하는줄 알았다..
#힙함수에서 값을 음수화 시켜 최대힙 구하는 방법이 신박하군
import heapq
import sys

input=sys.stdin.readline
N=int(input())
nums=[int(input()) for _ in range(N)]

for i in range(1,N+1):
    pq_right = nums[:i]
    if len(pq_right)==1:
        print(pq_right[0])
        continue
    mid = len(pq_right) // 2
    pq_left=[]
    while len(pq_right)!=mid:
        a=pq_right.pop()
        heapq.heappush(pq_left,-a)
    heapq.heapify(pq_right)
    max_heap = heapq.heappop(pq_left)
    min_heap = heapq.heappop(pq_right)
    while -max_heap > min_heap:
        heapq.heappush(pq_left,-min_heap)
        heapq.heappush(pq_right,-max_heap)
        max_heap = heapq.heappop(pq_left)
        min_heap = heapq.heappop(pq_right)
    print(-max_heap)
