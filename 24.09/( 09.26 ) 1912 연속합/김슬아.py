# 틀렸읍니다..
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
n=int(input())
nums=list(map(int,input().split()))

sort_num=sorted(nums)

result_sum=[]
def continuous_sum(start,max_value):
    end = 0
    max_value = sort_num.pop()
    while nums[end] != max_value :
        end +=1
    if start > end:
        result_sum.append(sum(nums[end:start+1]))
    else:
        result_sum.append(sum(nums[start:end+1]))
        start = end
    if end == 0 or nums[end]==nums[-1]:
        return
        
    continuous_sum(start,max_value)

start = 0
max_num = sort_num.pop()
result_sum.append(max_num)
while nums[start] != max_num :
    start +=1
continuous_sum(start,max_num)

print(max(result_sum))
