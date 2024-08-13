import sys
input = sys.stdin.readline

N = int(input())
# 높이 행렬
matrix = [[] for _ in range(N)] 
for _ in range(N):
    matrix[_] = list(map(int, input().split()))

# 안전영역 최대 개수 커지다 작아짐
pre = 0
now = 1
standard = 4

count = 0
safeB = 0
safeT = [0 for _ in range(N)]


def isSafe(i, j):
    if matrix[i][j] > standard:
        return 1

def checkPre(i, j):
    for k in range(j, 0, -1):
        if matrix[i][k] > standard:
            matrix[i][k] = standard
        else:
            break
    if i != 0 and isSafe(i-1, k-1):
        checkT(i-1, k-1)
    if i != N-1 and isSafe(i+1, k-1):
        checkB(i+1, k-1)

def checkF(i, j):
    for k in range(j, N):
        if matrix[i][k] > standard:
            matrix[i][k] = standard
        else:
            break
    if i != 0 and isSafe(i-1, k-1):
        checkT(i-1, k-1)
    if i != N-1 and isSafe(i+1, k-1):
        checkB(i+1, k-1)

def checkB(i, j):
    for k in range(i, N):
        if matrix[k][j] > standard:
            matrix[k][j] = standard
        else:
            break
    if k != N-1 and isSafe(i, k+1):
        checkF(i, k+1)
    if k != 0 and isSafe(i, k-1):
        checkPre(i, k-1)

def checkT(i, j):
    for k in range(i, 0, -1):
        if matrix[k][j] > standard:
            matrix[k][j] = standard
        else:
            break
    if j != 0 and isSafe(i, k-1):
        checkPre(i, k-1)
    if j != N-1 and isSafe(i, k+1):
        checkF(i, k+1)

# 완전 탐색
for i in range(N):
    safeB = 0
    for j in range(N):
        # 안전 영역
        if isSafe(i, j):
            count+=1

            if j != N-1 and isSafe(i, j+1):
                checkF(i, j+1)
            if i != N-1 and isSafe(i+1, j):
                checkB(i+1, j)
            if i != 0 and isSafe(i-1, j):
                checkT(i-1, j)
            

            # 이전 것이 안전하지 않으면 +1
        #     if safeB or safeT[j] or matrix[i+1][j] > standard:
        #         count -= 1
        #     safeB = 1
        #     safeT[j] = 1
        # else:
        #     #물에 잠김
        #     safeB = 0
        #     safeT[j] = 0
now = count

# while (now >= pre):
#     pre = now

#     count = 0
#     safeB = 0
#     safeT = [0 for _ in range(N)]

#     # 완전 탐색
#     for i in range(N):
#         safeB = 0
#         for j in range(N):
#             # 안전 영역
#             if matrix[i][j] > standard:
#                 count+=1
#                 # 이전 것이 안전하지 않으면 +1
#                 if safeB or safeT[j] or matrix[i+1][j]:
#                     count -= 1
#                 safeB = 1
#                 safeT[j] = 1
#             else:
#                 #물에 잠김
#                 safeB = 0
#                 safeT[j] = 0
#     now = count

#     standard += 1

# 행렬 출력
for m in matrix:
    print(m)

# 안전 영역의 최대 개수
print(standard)
print(now)
print(pre)

# 비의 양 -> 일정 높이 이후 지점 물에 잠김
