import sys
input = sys.stdin.readline

n = int(input())

numbers = list(map(int, input().split()))

result = []
plus = 0
for num in numbers:
    if num < 0:
        result.append(plus)
    plus+=num
    if plus <= 0:
        plus = 0

if result and max(result) == 0:
    print(max(numbers))
elif result:
    print(max(result))
else:
    print(plus)