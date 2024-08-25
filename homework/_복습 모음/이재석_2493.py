import sys

read = sys.stdin.readline

n = int(read().strip())
bld_list = list(map(int,read().strip().split()))

stack = []
for i in range(n):
    if stack and stack[-1][0] > bld_list[i]:
        max_bld = stack.pop()
        print(max_bld[1]+1)

    else:
        print(0)

    stack.append([bld_list[i], i])
