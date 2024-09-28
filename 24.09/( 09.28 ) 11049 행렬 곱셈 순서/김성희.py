import sys
input = sys.stdin.readline

N = int(input())
size = []
for _ in range(N):
    size.append(list(map(int, input().split())))

def cal(A, B):
    n = A[0]
    m = A[1]
    k = B[1]
    
    return n * m * k

dp = [0] * N
def bind(A, B, C, dp, i):
	n = A[0]
	m = A[1]
	k = B[1]
	s = C[1]
    
	if not dp:
		result = cal(A, B) + n * k * s
		dp.append(result)
	else :
		dp[-1] += n * k * s
		# temp = bind(A, B, [B[0], s], [], i)
		# result = min(temp) + cal(B, C)
		# dp.append(result)
	result = n * m * s + cal(B, C)
	dp.append(result)
	if i != N -1 :
		dp = bind(A, C, size[i+1], [min(dp)], i+1)
	return dp
 
# dp = bind(size[0], size[1], size[2], dp, 2)

print(dp)
print(min(dp))