import sys

size = int(sys.stdin.readline())
stack = []
nums = ""
result = ""
ans = ""

for i in range(size):
    nums += sys.stdin.readline() + ""

for i in range(1, size + 1):
    if not stack or stack[-1] > i:
        stack.append(i)
        ans += "+\n"
    else:
        result += str(stack.pop()) + ""
        ans += "-\n"

if nums == result:
    sys.stdout.write(ans)

else:
    sys.stdout.write("NO")
