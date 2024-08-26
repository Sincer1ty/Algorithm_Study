#로직은맞는데 최적화문제로 시간초과 났습니다..ㅠㅠ
import sys
input=sys.stdin.readline
# 선분의 개수  N
N=int(input())
# 선분들 이중리스트로 만듬
lines =[list(map(int,input().split())) for _ in range(N)]
# 주어진 선분 길이
D = int(input())
# 선분들이 길이를 저장 할 리스트
length=[]
# 최대수
max_count=0

# 선분 d 안에 포함된 선의 개수를 찾는 함수 , k는 선분들의 왼쪽 끝점
def countMaxLine(k):
    count=0
    for j in range(N):
        if lines[j][0]>=k and lines[j][1]<=k+D:
            count+=1
    return count
# 먼저 이중리스트 요소 안의 요소를 오름차순으로 정렬 countMaxLine의 k 값을 왼쪽으로 다 보내버리기 위해
for i in range(N):
    if lines[i][0]>lines[i][1]:
        lines[i][0],lines[i][1] =lines[i][1],lines[i][0]
    # 길이들 length리스트에 넣음
    length.append(abs(lines[i][1]-lines[i][0]))
# 리스트의 최소길이보다 D 길이가 작을경우 최대개수는 0일것이므로 0 반환
if D < min(length):
    print(0)
else:
    for i in range(N):
        # 왼쪽 끝점 기준으로 함수 실행
        count=countMaxLine(lines[i][0]) 
        # 함수결과값 최대값 갱신
        if max_count < count:
            max_count = count
    print(max_count)
