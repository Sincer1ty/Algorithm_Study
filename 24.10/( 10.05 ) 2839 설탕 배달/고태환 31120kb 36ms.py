# N에서 5씩 빼다가 3의 배수로 나눠지면 봉지 개수 업뎃
bag = -1
five=0
N=int(input())
temp=N
if temp%5==0:
    print(temp//5)
else:
    while N > 0:
        if N%3==0:
            bag=five+N//3
        N-=5
        five+=1
    print(bag)