import sys
input = sys.stdin.readline

# from collections import deque

# queue = deque()

# queue = deque(input())

# 스택 사용
string = input().strip()

stack = []
exp = []
result = 0
num = 1
for s in string:
    if s == '(' or s == '[':
        stack.append(s)
        # if exp[-1] != '+' or exp[-1] !='*':
        if num != 1:
            result += num
            num = 1
            # exp.append('+')
    else :
        peek = stack.pop()
        if peek == '(':
            if s == ')':
                num *= 2
                exp.append(2)
        elif peek == '[':
            if s == ']':
                num *= 3
                exp.append(3)
    pre = s

print(result)

# while stack:
#     s = stack.pop()

#     if s == '(':
#         exp.append(3)
#     elif s == '[':
#         exp.append(2)
#     else :
#         continue

#     if s[-1] == ')' or s[-1] == ']':
#         exp.append('*')
#     elif s[-1] == '(' or s[-1] == '[':
#         exp.append('+')

# print(stack)


# 정수 출력

# 올바르지 못하면 0