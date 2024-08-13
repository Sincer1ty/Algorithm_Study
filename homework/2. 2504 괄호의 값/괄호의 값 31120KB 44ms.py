#다 보고 했음니다..
#접근법
#괄호 유효성 검사 -> c언어 스택 큐 7번 참고
#괄호 값 계산은 클로드 도움 받음
brackets=input()

stack=[]
stack_num=[0]
# valid = True 값 유효한 지 검사
for bracket in brackets:
    if(bracket == "(" or bracket == "["):
        stack.append(bracket)
        stack_num.append(0)
    elif bracket == ")":
        # 스택이 비었거나 스택 제일 끝 값이 "(" 이 아니면
        if not stack or stack[-1] != "(":
            valid = False
            #포문탈출
            break
        stack.pop()
        temp = stack_num.pop()
        if(temp==0):
            stack_num[-1] += 2
        else:
            stack_num[-1] += temp*2
    elif(bracket =="]"):
        # 스택이 비었거나 스택 제일 끝 값이 "[" 이 아니면
        if not stack or stack[-1] != "[":
            valid = False
            #포문탈출
            break
        stack.pop()
        temp = stack_num.pop()
        if(temp==0):
            stack_num[-1] += 3
        else:
            stack_num[-1] += temp*3
if valid and len(stack)==0:
    print(stack_num[0])
else:
    print(0)
