N=int(input())
city = [[0]*(N+1) for _ in range(N+1)]

cases_num = int(input())
result =0
police= []
for _ in range(cases_num):
    x,y=map(int,input().split())
    a=(x-1)+(y-1)
    b=(N-x)+(N-y)
    if city[x][y]==0:
        city[x][y] = result
        result +=min(a,b)
    if a<=b:
        police.append(1)
    else:
        police.append(2)
    city[x][y]=1
print(result,sep='\n')
print(*police, sep='\n')
