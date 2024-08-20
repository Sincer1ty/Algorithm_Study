import sys
from collections import deque

board = int(sys.stdin.readline())
apple_nums = int(sys.stdin.readline())
apple_location = [[]]
for _ in range(apple_nums):
    apple_location.append(list(map(int, sys.stdin.readline().split())))

turn = [""] * 10000
turn_nums = int(sys.stdin.readline())
for _ in range(turn_nums):
    turning_point = list(map(str, sys.stdin.readline().split()))
    turn[int(turning_point[0])] = turning_point[1]

snake = deque()
time_cnt = 0
row, col = 1, 1
snake.append([row, col])

while row <= board and col <= board:
    time_cnt += 1

