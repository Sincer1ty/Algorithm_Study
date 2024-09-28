import sys

read = sys.stdin.readline


# 5*3
# 3*2
# 2*6

n = int(read().strip())

num_list = []
dp = [[0 for _ in range(n)]for _ in range(n)]

for i in range(n):
    x, y = map(int,read().strip().split())
    num_list.append([x,y])

sum = 0
for i in range(1,n):
    for j in range(0,n-i):
        if i ==1:
            dp[j][j+1] = num_list[j][0] * num_list[j][1] * num_list[i+1][1]
            continue
        
        dp[j][j+1] = 2**32

        for k in range(j,j+i):
            dp[j][j+i] = min(dp[j][j+i], dp[j][k] + dp[k+1][j+i] + num_list[k][0]* num_list[k][1]* num_list[j+i][1])


        # temp = num_list[i][0] * num_list[i][1] * num_list[i+1][1] 
        # sum += temp 

print(num_list)
print(dp)
