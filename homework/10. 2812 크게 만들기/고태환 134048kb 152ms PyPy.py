import sys
input = sys.stdin.readline
N, K = map(int, input().split())
num = str(input())
stack = []
cnt = 0
for n in num:
    while stack:
        if stack[-1] >= n or cnt == K:
            break
        stack.pop()
        cnt += 1
    stack.append(n)
str = ""
if cnt == K:
    for s in stack:
        print(s, end="")
else:
    for s in range(N-K):
        print(stack[s], end="")
