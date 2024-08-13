import sys
input = sys.stdin.readline
brackets = list(input().strip())
stack=[]

# 유효한 괄호열인지 확인
for brkt in brackets:
    if stack:
        if stack[-1] == '(' and brkt == ')':
            stack.pop()
            continue
        elif stack[-1] == '[' and brkt == ']':
            stack.pop()
            continue
    stack.append(brkt)

if stack:
    print(0)
else:
    for brkt in brackets:
        if brkt == ')':
            if stack[-1] == '(':
                stack.pop()
                stack.append(2)
            else:
                piece = 0
                while(stack[-1] != '('):
                    piece += stack.pop()
                stack.pop()
                stack.append(2 * piece)
        elif brkt == ']':
            if stack[-1] == '[':
                stack.pop()
                stack.append(3)
            else:
                piece = 0
                while(stack[-1] != '['):
                    piece += stack.pop()
                stack.pop()
                stack.append(3 * piece)
        else:
            stack.append(brkt)

    print(sum(stack))