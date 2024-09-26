import sys
sys.setrecursionlimit(100000)

size = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().strip().split()))
sum_nums = sum(nums)


def find_max(start, end, check_sum, max_sum):
    if end <= start:
        return max_sum

    if check_sum - nums[start] < check_sum - nums[end]:
        if max_sum < check_sum - nums[end]:
            max_sum = check_sum - nums[end]
        return find_max(start, end - 1, check_sum - nums[end], max_sum)

    else:
        if max_sum < check_sum - nums[start]:
            max_sum = check_sum - nums[start]
        return find_max(start + 1, end, check_sum - nums[start], max_sum)


print(find_max(0, size - 1, sum_nums, sum_nums))
