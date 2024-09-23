# 시간초과 메모리초과로 인해 메모이제이션 부분 클로드 도움 받음
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N=int(input())
M=int(input())
parts={}
parts_m=set()
answer={}
for _ in range(M):
    X,Y,K = map(int,input().split())
    parts_m.add(X)
    if X not in parts:
        parts[X]={}
    parts[X][Y]=K
# 메모이제이션을 위한 딕셔너리
memo = {}

def assemble(num):
    # 이미 계산된 결과가 있으면 반환
    if num in memo:
        return memo[num]
    
    # 기본 부품일 경우 자기 자신 1개만 필요하므로 1 반환
    if num not in parts_m:
       return {num:1}
    
    # 현재 부품의 조립 결과를 저장할 딕셔너리를 초기화
    result = {}
    # 중간 부품인 경우 필요한 하위 부품에 대해 재귀적으로 계산
    # num을 만드는 데 필요한 각 하위 부품과 그 개수에 대해 반복
    for part,count in parts[num].items():
        # 각 하위 부품에 대해 재귀적으로 assemble 함수를 호출
        sub_result = assemble(part)
        for sub_part, sub_count in sub_result.items():
            result[sub_part] = result.get(sub_part,0) + sub_count *count

    memo[num] =result # 계산 결과를 메모에 저장
    return result

answer = assemble(N)

for key,value in sorted(answer.items()):
    print(f"{key} {value}")
