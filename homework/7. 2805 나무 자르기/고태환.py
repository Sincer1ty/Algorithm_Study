import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
pl, pr = 0, max(arr)
while(pl <= pr):
    res=0
    p = (pl+pr)//2
    for h in arr:
        if h-p > 0:
            res+=(h-p)
    if M > res:
        pr = p-1
    elif M < res:
        pl = p+1
    else:
        break
if M > res:
    print(p-1)
else:
    print(p)
        
# 실수 1. 0이 아니라 min으로 잡음
# 실수 2. 자르는 높이가 높을수록 양이 많아질거라고 생각함
# 실수 3. '최소한' M 은 잘라가야 하는데 결과 중에 부족한 경우 생김 
