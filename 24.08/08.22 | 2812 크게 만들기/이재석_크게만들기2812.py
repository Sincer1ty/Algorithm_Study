import sys
read = sys.stdin.readline

n, k = map(int,read().strip().split())
give_num = read().strip()

stack = []
for i in range(len(give_num)):
    # print(give_num[i])
    while stack and stack[-1] < give_num[i] and k>0:
        stack.pop()
        k-=1
    stack.append(give_num[i])

if k>0:
    stack = stack[:-k]

print(''.join(stack))

