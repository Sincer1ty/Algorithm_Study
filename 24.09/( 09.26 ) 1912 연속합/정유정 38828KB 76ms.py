import sys

size = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().strip().split()))
sum_nums = max_nums = nums[0]

for i in range(size - 1):
    sum_nums += nums[i + 1]
    if sum_nums < nums[i + 1]:
        sum_nums = nums[i + 1];
    if sum_nums > max_nums:
        max_nums = sum_nums

print(max_nums)
