import sys
sys.setrecursionlimit(10000000)

size = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split()))

memo = [[-1] * size for _ in range(size)]
# print(memo)


def recur(left: int, right: int)-> int:
    if left > right:
        return 0
    if memo[left][right] != -1:
        return memo[left][right]

    if nums[left] == nums[right]:
        memo[left][right] = recur(left + 1, right - 1) + 1
    else:
        memo[left][right] = min(recur(left + 1, right) + 1, recur(left, right - 1) + 1)

    return memo[left][right]


print(recur(0, size - 1))
