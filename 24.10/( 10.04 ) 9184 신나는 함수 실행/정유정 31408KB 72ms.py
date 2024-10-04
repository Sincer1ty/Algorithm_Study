import sys

memo = {}
num1, num2, num3 = map(int, sys.stdin.readline().strip().split())


def recur(a: int, b: int, c: int)->int:
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if (a, b, c) in memo:
        return memo.get((a, b, c))

    if a > 20 or b > 20 or c > 20:
        memo[(a, b, c)] = recur(20, 20, 20)
        return memo.get((a, b, c))

    if a < b < c:
        memo[(a, b, c)] = recur(a, b, c - 1) + recur(a, b - 1, c - 1) - recur(a, b - 1, c)
        return memo.get((a, b, c))

    memo[(a, b, c)] = (recur(a - 1, b, c) + recur(a - 1, b - 1, c) +
                        recur(a - 1, b, c - 1) - recur(a - 1, b - 1, c - 1))
    return memo.get((a, b, c))


while num1 != -1 or num2 != -1 or num3 != -1:
    print("w(" + str(num1) + ", " + str(num2) + ", " + str(num3) + ") = " + str(recur(num1, num2, num3)))
    num1, num2, num3 = map(int, sys.stdin.readline().strip().split())
