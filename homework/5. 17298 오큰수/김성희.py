import sys
input = sys.stdin.readline

# 수열의 크기
N = int(input())

A = list(map(int, input().split()))

# 오큰수
def NGE(i):
    for j in range(i+1, N):
        if A[i] < A[j]:
            return A[j]
    return -1

for i in range(N):
    result = NGE(i)
    print(result, end=" ")
