import sys

tree_nums, std_sum = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

start = 1
end = max(trees)
ans_height = (start + end) // 2
check_sum = 0

while start <= end:
    check_sum = 0

    for i in trees:
        if i > ans_height:
            check_sum += i - ans_height

    if std_sum == check_sum:
        break
    elif std_sum > check_sum:
        end = ans_height - 1
    else:
        start = ans_height + 1

    ans_height = (start + end) // 2

sys.stdout.write(str(ans_height))
