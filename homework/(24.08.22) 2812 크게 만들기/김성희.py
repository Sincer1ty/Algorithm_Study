import sys
input = sys.stdin.readline

# N 자리에서 K 개 삭제
N, K = map(int, input().split())

# 문자열
number = list(input().strip())

stk = []
pre = int(number[0])
for i, n in enumerate(number):
    if K == 0:
        break

    if int(n) > pre:
        K -=1
    else:
        stk.append(pre)
    
    if stk and stk[-1] < int(n):
        stk.pop()

    pre = int(n)

stk.extend(number[i:])
# result.append(int(number[-1]))
print(*stk, sep="")