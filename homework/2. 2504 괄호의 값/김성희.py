import sys
input = sys.stdin.readline

# from collections import deque

# queue = deque()

# queue = deque(input())

# 스택 사용
string = input().strip()

stack = []
num = 0
exp = []
for s in string:
    if s == '(' or s == '[':
        stack.append(s)
        exp.append('+')
    else :
        peek = stack[-1]
        if peek == '(':
            if s == ')':
                exp.append(2)
        elif peek == '[':
            if s == ']':
                exp.append(3)
        



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