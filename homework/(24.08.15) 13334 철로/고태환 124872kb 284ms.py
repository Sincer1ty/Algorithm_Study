import sys
input = sys.stdin.readline
import heapq
N=int(input())
ho=[]
# 좌표 정보 넣기
for _ in range(N):
    a, b = map(int,input().split())
    ho.append((min(a,b),max(a,b)))
# 좌표 정보 정렬하기
ho.sort(key=lambda x: x[1])
L = int(input())
m=0
cnt=[]
for se in ho:
    s,e=se
    heapq.heappush(cnt,s)
    # 자신의 종료점부터 L만큼보다 앞에 있는 점들 빼내기
    while(cnt and cnt[0] < e-L):
        heapq.heappop(cnt)
    m=max(m,len(cnt))
print(m)