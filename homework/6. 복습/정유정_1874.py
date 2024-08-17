import sys

size = int(sys.stdin.readline())
stack = []
nums = []
result = []
ans = ""

for i in range(size):
    nums.append(int(sys.stdin.readline()))

idx = 0
for i in range(1, size + 1):
    if i > nums[idx]:
        while stack and nums[idx] == stack[-1]:
            result.append(stack.pop())
            idx += 1
            ans += "-\n"

        stack.append(i)
        ans += "+\n"

    else:
        stack.append(i)
        ans += "+\n"

while stack:
    result.append(stack.pop())
    idx += 1
    ans += "-\n"

if nums == result:
    sys.stdout.write(ans)

else:
    sys.stdout.write("NO")
