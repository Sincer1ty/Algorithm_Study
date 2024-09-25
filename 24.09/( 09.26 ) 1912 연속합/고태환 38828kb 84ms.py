n=int(input())
seq=list(map(int,input().split()))
Min = 0
temp = 0
Sum = 0
res = -float('inf')
for num in seq:
    Sum+=num # 그래프 경로
    temp+=num # 부분합
    res = max(res, temp)
    if Min > Sum: # 최소가 갱신되면 부분합 초기화 
        Min = Sum
        temp = 0
print(res)