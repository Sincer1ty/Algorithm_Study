import sys
input = sys.stdin.readline

# 스택 사용
string = input().strip()

stack = []
r = []
result = 0
num = 1
for s in string:
    if s == '(' or s == '[':
        stack.append(s)
        if num != 1:
            result += num
            num = 1
    else :
        peek = stack.pop()
        if peek == '(':
            if s == ')':
                if stack:
                    num *= 2
                else:
                    result += num
                    num = 1
                    result *= 2
                    r.append(result)
                    result = 0
        elif peek == '[':
            if s == ']':
                if stack:
                    num *= 3
                else:
                    result += num
                    num = 1
                    result *= 3
                    r.append(result)
                    result = 0

# 정수 출력
print(sum(r))

# 올바르지 못하면 0