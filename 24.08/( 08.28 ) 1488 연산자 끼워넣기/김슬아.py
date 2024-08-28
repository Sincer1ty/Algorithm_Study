from itertools import permutations
import sys
input=sys.stdin.readline
N=int(input())

nums=list(map(int,input().split()))

oper_num=list(map(int,input().split()))

operators = []
operator_types = ['+', '-', '*', '/']
for op, count in zip(operator_types, oper_num):
    operators.extend([op] * count)
all_oper_permutations = set(permutations(operators,N-1))

def caculate(num1,num2,op):
    if op=='+':
        return num1+num2
    elif op=='-':
        return num1-num2
    elif op=='*':
        return num1*num2
    else:
        if num1<0:
            return -((-num1)//num2)
        else:
            return num1//num2
# - 무한대로 초기화
max_result=float('-inf')
# + 무한대로 초기화
min_result=float('inf')

for oper_perm in all_oper_permutations:
    result=nums[0]
    for i in range(N-1):
        result=caculate(result,nums[i+1],oper_perm[i])
    max_result=max(max_result,result)
    min_result=min(min_result,result)
print(max_result)
print(min_result)


# 재귀 방식
N=int(input())

nums=list(map(int,input().split()))

oper_num=list(map(int,input().split()))

def caculate(num1,num2,operator_index):
    if operator_index==0:
        return num1+num2
    elif operator_index==1:
        return num1-num2
    elif operator_index==2:
        return num1*num2
    elif operator_index==3:
        if num1<0:
            return -((-num1)//num2)
        else:
            return num1//num2

# - 무한대로 초기화
max_result=float('-inf')
# + 무한대로 초기화
min_result=float('inf')

def result(caculate_result,next_oper_index,remaining_oper_count):
    global max_result,min_result,oper_num

    if next_oper_index ==N-1:
        max_result=max(max_result,caculate_result)
        min_result=min(min_result,caculate_result)
        return
    for i in range(4):
        if remaining_oper_count[i] >0:
            remaining_oper_count[i] -=1
            next_result=caculate(caculate_result,nums[next_oper_index+1],i)
            result(next_result,next_oper_index+1,remaining_oper_count)
            # 백트래킹
            remaining_oper_count[i]+=1

result(nums[0],0,oper_num)
print(max_result)
print(min_result)
