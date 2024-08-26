import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
stack=[]
# 오른쪽에서 왼쪽으로 쭉 진행한다
for i in range(N-1,-1,-1):
    n = A[i]
    # 오큰수랑 비교해서 원래 수열에선 오큰수로 기록해버린 다음
    noks = True
    for j in range(len(stack)-1,-1,-1):
        if stack[j] > n:
            noks = False
            A[i] = stack[j]
            break
    if noks:
        A[i] = -1
    # 스택에서 자기보다 약하거나 같은 놈들 다 죽여버린다
    while(len(stack)>1 and stack[-1] <= n):
        stack.pop()
    # 스택에 냅다 넣는다
    stack.append(n)

    # 스택 맨 위 peek하면 그게 오큰수
for a in A:
    print(a,end=' ')