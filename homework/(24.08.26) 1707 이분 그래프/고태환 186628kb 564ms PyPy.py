import sys
input = sys.stdin.readline
K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    Vcolor = [0]*V
    Vdict = {i : [] for i in range(V)}
    # 간선 받아
    for _ in range(E):
        s, e = map(int, input().split())
        Vdict[s-1].append(e-1)
        Vdict[e-1].append(s-1) # << 놓쳤었던 부분
    # 간선 순회해
    is2m = True
    for i in range(V):
        if Vcolor[i] == 0: # 방문 안 한 점이라면 dfs 시작
            Vcolor[i] = 1
            stack = [i] # dfs에 쓸 스택
            while(stack and is2m):
                j = stack.pop()
                for k in Vdict[j]: # 딕셔너리에 있는 간선들 전부 방문
                    if Vcolor[k]==0: # 방문 안 한 정점 찾았으면 스택에 해당 정점 추가하고 반대 색깔 색칠
                        stack.append(k)
                        Vcolor[k] = -Vcolor[j]
                    elif Vcolor[k] == Vcolor[j]: # 이분 그래프가 아니었다면 종료
                        is2m = False
                        break
    if is2m:
        print("YES")
    else:
        print("NO")
    