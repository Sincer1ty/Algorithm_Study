N,C=map(int,input().split())
houses=[int(input()) for _ in range(N)]
houses.sort()
min_dist = houses[1]-houses[0]
max_dist = houses[-1]-houses[0]

distaces=[]
for i in range(1,N):
    # 포문돌면서 경우의 수 거리값 저장
    distaces.append(houses[i]-houses[0])
k=0
while min_dist<max_dist:
    wifi=[]
    count=0
    i=0
    while i!=N:
        j=0
        cur_house = houses[i]
        if i==0:
            pre_wifi=0
            pre_house=0
        else:
            # 이전공유기 설치 지점
            pre_house = houses[pre_wifi]
        close_dist=cur_house-pre_house
        if close_dist>=min_dist:
            # 공유기 개수 저장
            count+=1
            # 길이저장
            pre_wifi=i
            wifi.append(close_dist)
        else:
            j+=1
        i+=1
    k+=1
    min_dist = distaces[k]


        
