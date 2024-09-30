import sys
sys.setrecursionlimit(1000000)

num = int(sys.stdin.readline())
memo = [-1 for _ in range(num + 1)]
memo[0] = memo[1] = 0


def find_one(num):
    if memo[num] == -1:
        if num % 6 == 0:
            memo[num] = min(find_one(num // 3), find_one(num // 2), find_one(num - 1)) + 1

        elif num % 3 == 0:
            memo[num] = min(find_one(num // 3), find_one(num - 1)) + 1

        elif num % 2 == 0:
            memo[num] = min(find_one(num // 2), find_one(num - 1)) + 1

        else:
            memo[num] = find_one(num - 1) + 1
    return memo[num]


print(find_one(num))
