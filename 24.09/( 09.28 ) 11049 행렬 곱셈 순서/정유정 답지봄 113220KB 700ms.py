import sys

size = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(size)]

memo = [[0] * size for _ in range(size)]

# for i in range(size - 1):
#     memo[i][i] = 0
#     memo[i][i + 1] = matrix[i][0] * matrix[i][1] * matrix[i + 1][1]

for length in range(1, size):
    for start in range(size - 1):
        if start + length >= size:
            break

        end = start + length
        memo[start][end] = int(1e9)

        for i in range(start, end):
            memo[start][end] = min(memo[start][end],
                                   memo[start][i] + memo[i + 1][end]
                                   + (matrix[start][0] * matrix[i][1] * matrix[end][1]))

print(memo[0][size - 1])
