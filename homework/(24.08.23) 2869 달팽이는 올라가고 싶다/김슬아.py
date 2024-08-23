import sys
import math
input=sys.stdin.readline
A,B,V=map(int,input().split())
# 수학공식으로 해결하는 게 신기방기
# 낮에 처음 올라가고 나머지 거리/하루치 거리 해서 일수를 구함 
# ceil로 소수점 이하를 올림하여 정확한 일수 계산
# 마지막 날 달팽이 올라가는 것 +1
days=math.ceil((V-A)/(A-B))+1

print(days)

# import sys

# input = sys.stdin.readline
# A, B, V = map(int, input().split())
# day = 0

# if A >= V:  # 첫날에 바로 도달하는 경우
#     print(1)
# elif A - B == 1:
#     day = V - A  # A-B가 1일 때의 특수한 경우
#     print(day + 1)  # 마지막 날 추가
# else:
#     while V > 0:
#         day += 1
#         V -= A
#         if V <= 0:  # 정상에 도달하거나 넘어선 경우
#             break
#         V += B
#     print(day)

# import sys
# input=sys.stdin.readline
# A,B,V=map(int,input().split())
# day=0
# if A-B ==1:
#     V=V-B
#     print(V)
# else:
#     while V>1:
#         V=V-A+B
#         day+=1
#     print(day)

