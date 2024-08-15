import sys
import heapq

read= sys.stdin.readline
locations = []

n = int(read().strip())

for i in range(n):
    hmofc_list = list(map(int ,read().strip().split()))
    #집, 사무실의 숫자를 작은 순서부터 정렬
    locations.append(hmofc_list)

d = int(read().strip())

#끝점을 기준으로 locations 리스트 정렬


heap = []
max_cnt = 0

for location in locations:
    start, end= location 
    heapq.heappush(heap, start)

