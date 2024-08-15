import sys
input = sys.stdin.readline

n = int(input())

trail = []
for _ in range(n):
    home, office = map(int, input().split())
    if home > office:
        home, office = office, home
    trail.append([home, office])

trail.sort()

# 철로의 길이 : d
d = int(input())

result = 0

while trail:
    trailS = trail[0][0]
    trailE = trailS + d

    # 집 & 사무실 모두 철로에 포함되는 최대 사람 수 구하기
    count = 0

    for home, office in trail:
        if home < trailE:
            if home == trailS:
                trail.pop(0)

            if office <= trailE:
                count += 1
        else:
            break

    if result < count:
        result = count

print(result)
