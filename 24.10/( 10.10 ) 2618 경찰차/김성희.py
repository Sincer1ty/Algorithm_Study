import sys
input = sys.stdin.readline

N = int(input())
W = int(input())
# 큐?
accident = []
distance = []
fr = []
for _ in range(W):
    x, y = map(int, input().split())
    accident.append([x, y])
    distance.append(float('inf'))
    fr.append([0,0])

police1 = [1, 1]
police2 = [N, N]

# city = [[0 for _ in range(N)] for _ in range(N)]
compare=[police1, police2]
for i, a in enumerate(accident):
    for c in compare:
        if distance[i] > abs(c[0]-a[0]) + abs(c[1]-a[1]):
            distance[i] = abs(c[0]-a[0]) + abs(c[1]-a[1])
            fr[i] = c
        # 같으면 fr에 추가해야 될까..
    compare.append(a)

def check(i):
    check(fr[i])
    pass

check(W-1)

print(sum(distance))
print(fr)
# distance = 0
# call = []
# for a in accident:
#     distance += min(abs(police1[0]-a[0]) + abs(police1[1]-a[1]), abs(police2[0]-a[0]) + abs(police2[1]-a[1]))
#     if abs(police1[0]-a[0]) + abs(police1[1]-a[1]) < abs(police2[0]-a[0]) + abs(police2[1]-a[1]):
#         police1 = a
#         call.append(1)
#     else:
#         police2 = a
#         call.append(2)

# print(distance)
# for c in call:
#     print(c)