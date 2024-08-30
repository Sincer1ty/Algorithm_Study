import copy
import sys
sys.setrecursionlimit(10**4)

R, C = map(int, input().split())

# 문자열 뜯어서 받기 힘들다
twMap = [[0 for _ in range(C)] for _ in range(R)]
Sx, Sy = 0, 0
for i in range(R):
    temp = input()
    for j in range(C):
        twMap[i][j] = temp[j]
for i in range(R):
    for j in range(C):
        if twMap[i][j] == 'S':
            Sx, Sy = i,j

# 고슴도치 퍼뜨리고
# 홍수 퍼뜨리기

arrived = False
cnt = 0

while(1):
    # 고슴도치 움직임
    moved = False
    for i in range(R):
        for j in range(C):
            if twMap[i][j] == 'S':
                if i+1 < R and twMap[i+1][j] == '.':
                    twMap[i+1][j] = -2
                    moved = True
                if 0 <= i-1 and twMap[i-1][j] == '.':
                    twMap[i-1][j] = -2
                    moved = True
                if j+1 < C and twMap[i][j+1] == '.':
                    twMap[i][j+1] = -2
                    moved = True
                if 0 <= j-1 and twMap[i][j-1] == '.':
                    twMap[i][j-1] = -2
                    moved = True
                if i+1 < R and twMap[i+1][j] == 'D':
                    arrived = True
                if 0 <= i-1 and twMap[i-1][j] == 'D':
                    arrived = True
                if j+1 < C and twMap[i][j+1] == 'D':
                    arrived = True
                if 0 <= j-1 and twMap[i][j-1] == 'D':
                    arrived = True
    
    for i in range(R):
        for j in range(C):
            if twMap[i][j] == -2:
                twMap[i][j] = 'S'

    # 티떱숲 홍수 갱신 (중복 계산 조심)
    for i in range(R):
        for j in range(C):
            if twMap[i][j] == '*':
                if i+1 < R and (twMap[i+1][j] == '.' or twMap[i+1][j] == 'S'):
                    twMap[i+1][j] = -1
                if 0 <= i-1 and (twMap[i-1][j] == '.' or twMap[i-1][j] == 'S'):
                    twMap[i-1][j] = -1
                if j+1 < C and (twMap[i][j+1] == '.' or twMap[i][j+1] == 'S'):
                    twMap[i][j+1] = -1
                if 0 <= j-1 and (twMap[i][j-1] == '.' or twMap[i][j-1] == 'S'):
                    twMap[i][j-1] = -1
    
    for i in range(R):
        for j in range(C):
            if twMap[i][j] == -1:
                twMap[i][j] = '*'
    
    cnt += 1 

    if arrived:
        break
    elif not moved:
        arrived = False
        break

if arrived:
    print(cnt)
else:
    print('KAKTUS')

