'''
#1st Try
import sys
read = sys.stdin.readline

n = int(read().strip())
num_input = list(map(int,read().strip().split()))
max = -1

for i in range(n):
    ismax = False
    max = num_input[i]
    for j in range(i+1, n):
        if num_input[i] < num_input[j]:
            max = num_input[j]
            print(max)
            ismax = True
            break
    
    if ismax == False:
        print(-1)
'''

#2nd Try

import sys
import heapq

read = sys.stdin.readline
n = int(read().strip())
num_input = list(map(int,read().strip().split()))

# Initialzing a Stack to store the idx of the NGE
# Storing largest index from i th number in num_input, and comparing it with the number on the right in num_list
stack = []
result = [-1] * n

for i in range(n):
    #Updating the stack with a bigger number on the right, everytime it finds one 
    while stack and num_input[stack[-1]] < num_input[i]:
        #Storing idx 
        idx = stack.pop()
        result[idx] = num_input[i]
    stack.append(i)

for res in result: 
    print(res)

#By putting the largest number in the stack where it stores the index, we are able to reduce the number of calculations to O(n)

'''
#3rd Try
import heapq
import sys

read = sys.stdin.readline
n = int(read().strip())
num_input = list(map(int,read().strip().split()))

min_heap = []
result = [-1] * n

for i in range(n):
    while min_heap and min_heap[0][0] < num_input[i]:
        value, idx = heapq.heappop(min_heap)
        result[idx] = num_input[i]

    heapq.heappush(min_heap, (num_input[i], i))    

for res in result:
    print(res)

'''