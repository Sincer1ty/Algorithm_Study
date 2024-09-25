import sys

part_num = int(sys.stdin.readline().strip())
part_connect = int(sys.stdin.readline().strip())
parts = [[] for _ in range(part_num + 1)]

mid_part_start = part_num

for _ in range(part_connect):
    part1, part2, num = map(int, sys.stdin.readline().strip().split())
    parts[part1].append([part2, num])
    if part1 < mid_part_start:
        mid_part_start = part1

basic_parts = [0 for _ in range(mid_part_start)]
calculated = []


def check_basic_part(part, num):
    global mid_part_start

    if part < mid_part_start:
        basic_parts[part] += num
        return

    if part in calculated:
        for check_p, check_n in calculated[part]:
            basic_parts[check_p] += check_n * num
        return

    for i in range(len(parts[part])):
        check_p, check_n = parts[part][i]
        check_basic_part(check_p, check_n * num)


for i in range(len(parts[part_num])):
    part, num = parts[part_num][i]

    if part < mid_part_start:
        basic_parts[part] += num
        continue

    check_basic_part(part, num)

idx = 1
for num in basic_parts[1:]:
    print(idx, num)
    idx += 1

