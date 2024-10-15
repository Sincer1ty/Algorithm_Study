# 읽을 수 있는 단어의 개수 최대
import sys
input = sys.stdin.readline

# K개의 글자
N, K = map(int, input().split())

words = []
sample = []
# 단어 총 N개
for _ in range(N):
	words.append(set(input().strip()))
	sample.append(words[-1])

letter = {'a', 'n', 't', 'i', 'c'}
# anta ~ tica
# antic 5개 필수
K-=5

# 중복이 가장 많은 글자 선택

while K > 0:
	if sample:
		w = min(sample, key=lambda x:len(x-letter))
		sample.remove(w)
	else:
		print(N)
		break
	w = w - letter
	for i in w:
		letter.add(i)
		K -= 1
		if K <= 0:
			break

if K < 0:
	print(0)
elif K == 0:
	# K개로만 이루어진 단어 있는지 찾고
	# 없으면 0
	count = 0
	for w in words:
		if len(w - letter) == 0:
			count+=1
	print(count)