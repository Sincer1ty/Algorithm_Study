import sys

daytime, nighttime, tree_height = map(int, sys.stdin.readline().split())

day = daytime - nighttime
check_day = tree_height // day

if tree_height % day != 0:
    sys.stdout.write(str(check_day + 1))
else:
    if ((check_day - 1) * day) + nighttime >= tree_height:
        sys.stdout.write(str(check_day - 1))
    else:
        sys.stdout.write(str(check_day))

