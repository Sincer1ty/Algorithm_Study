N,K=map(int,input().split())
number=list(input())
# 최종 숫자가 들어가는 stack
stack=[]
# 지운 숫자 개수 카운트
remove_count = 0

for i in range(N):
    # 지운숫자 개수가 K개 도달 안했고 stack에 값이 있고 스택 끝값이랑 number 배열 이랑 비교헸을 떼 number가 크다면
    while remove_count < K and stack and stack[-1] < number[i]:
        # 스택에서 팝하고 지웠으니 리무브 카운트 1올리기
        stack.pop()
        remove_count+=1
    # 조건 만족 못했으면 계속 넣기만 함
    stack.append(number[i])
# 위의 포문에서 아무것도 지우지 못했으면 stack에 넣은 수 뒤에서 부터 팝함
while remove_count < K:
    stack.pop()
    remove_count+=1
# 배열 다시 숫자로 합쳐주고 츨략
result = "".join(stack)
print(result)
