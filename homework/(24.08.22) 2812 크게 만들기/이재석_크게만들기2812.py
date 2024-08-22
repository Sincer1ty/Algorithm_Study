import sys
read = sys.stdin.readline
n, era = map(int,read().strip().split)
give_num = read().strip()


stack = []
for i in range(len(give_num)):
    # stack.append(give_num[i])
    while stack and stack[-1] < give_num[i] and era > 0:
        stack.pop()
        era -= 1
    stack.append(give_num[i])
    

