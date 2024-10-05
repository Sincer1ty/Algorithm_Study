import sys
sys.setrecursionlimit(1000000)

sugar = int(sys.stdin.readline().strip())
memo = [0] * (sugar + 1)


def sugar_deliver(sugar: int)-> int:
    if sugar == 0:
        return 0

    if sugar < 3:
        return 5000

    if memo[sugar] != 0:
        return memo[sugar]

    memo[sugar] = min(sugar_deliver(sugar - 5), sugar_deliver(sugar - 3)) + 1
    return memo[sugar]


sugar_deliver(sugar)
if memo[sugar] >= 5000:
    print(-1)
else:
    print(memo[sugar])
