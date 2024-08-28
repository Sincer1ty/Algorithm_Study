import sys

num_size = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
operators = list(map(int, sys.stdin.readline().split()))
max_val = -sys.maxsize - 1
min_val = sys.maxsize


def dfs(num: int, depth: int):
    global max_val, min_val

    if depth == num_size:
        max_val = max(num, max_val)
        min_val = min(num, min_val)
        return

    for i in range(4):
        if operators[i] != 0:
            operators[i] -= 1

            if i == 0 :
                dfs(num + nums[depth], depth + 1)
            elif i == 1:
                dfs(num - nums[depth], depth + 1)
            elif i == 2:
                dfs(num * nums[depth], depth + 1)
            else:
                dfs(int(num // nums[depth]), depth + 1)

            operators[i] += 1


dfs(nums[0], 1)
sys.stdout.write(str(max_val) + "\n")
sys.stdout.write(str(min_val) + "\n")
