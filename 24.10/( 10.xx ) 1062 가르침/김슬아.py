# 그리디방식으로 풀어서 밑의 반례 통과못함
# 4 10
# antahrtica
# antaxyztica
# antaxyktica
# antaxyutica
import sys
input = sys.stdin.readline
N,K=map(int,input().split())
# 가르칠 수 있는 언어가 a,n,t,i,c 추가적으로 없을 때 0 출력
words=[input().strip() for _ in range(N)]

cut_words=[]
for word in words:
    middle_part = word[4:-4]
    cut_words.append(middle_part)
def max_words(n):
    antatica_words="antic"
    if K-5<0:
        return 0
    for cut_word in cut_words:
        for i in range(len(cut_word)):
            if cut_word[i] not in antatica_words:
                if len(antatica_words)<K:
                    antatica_words+=cut_word[i]
                else:
                    n-=1
                    break
    return n
print(max_words(N))
