# 뒤에서 부터 읽은 문자열의 첫번째 문자가 앞읽 문자열에서 발견됐다면
# 그 다음 문자가 뒤읽 문자열의 다음 문자와 같은지 보고, 같지 않다면 탈락
# 앞읽 문자열의 마지막 문자까지 확인했다면 통과. 
# 문자열의 길이에서 통과한 문자열 빼면 답.
import sys
input = sys.stdin.readline
S = input().strip()
iS = ""
for i in range(len(S)-1,-1,-1): # 세번째 인자 빼먹어서 헤맴
    iS+=S[i]
while 1:
    i=0
    while i < len(S) and S[i]==iS[i]:
        i+=1
    if i==len(S):
        break
    else:
        S=S[1:] # 무지성으로 i+1부터 잘랐다가 한참 헤맴
print(2*len(iS)-len(S))