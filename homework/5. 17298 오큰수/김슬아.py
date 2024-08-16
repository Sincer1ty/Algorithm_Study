import sys

input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
# 오큰수가 없는 경우 -1을 출력
result = [-1] * N
# 아직 오큰수를 찾지 못한 원소들의 인덱스를 저장
stack = []

for i in range(N):
    while stack and nums[stack[-1]] < nums[i]:
        result[stack.pop()] = nums[i]
    stack.append(i)

print(*result)


# import sys
# input=sys.stdin.readline
# N=int(input())
# nums=list(map(int,input().split()))

# def maxnumleft(n):
#     k=nums[n]
#     stack=[]
#     for i in range(n+1,len(nums)):
#         if k<nums[i]:
#             stack.append(nums[i])
#     if stack:
#         return stack[0]
#     else:
#         return -1

# for i in range(N):
#     num = maxnumleft(i)
#     print(num,end=' ')
