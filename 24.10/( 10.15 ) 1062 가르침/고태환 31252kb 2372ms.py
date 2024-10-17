# a, n, t, i, c 이 다섯 글자는 필수적으로 들어감.
# 고로 K가 4 이하면 읽을 수 있는 단어 없음.
# 각 단어에 필요한 문자를 알게되면
# a, n, t, i, c 중에 하나라면 포함 안 시켜도 됨
# 그리디로 못 품 -> (필요한 글자수)C(K) 의 조합 중 골라야 됨.
# n의 제곱이라는 건데, 글자가 작아서 ㄱㅊ을듯
# 각 글자들을 세트에 넣은 후에 리스트로 변환하고 인덱스를 재귀로 조합 경우의 수
# 각 단어들은 딕셔너리로 취급?
# 종료 조건 달성 (가르칠 수 있는 글자 다 가르쳤을 때) 하면 단어 몇 개 읽을 수 있는지 체크

# 백트래킹으로 조합에 대한 경우의 수 따지기
def combi(idx,remain):
    global max_val
    if remain == 0:
        cnt = 0
        # 단어들을 순회하며 지금까지 가르친 글자들로 읽을 수 있는지 판별
        for word in words:
            cnt+=1
            for w in words[word]:
                if w not in storage: # 없는 글자가 있으면 cnt 원복
                    cnt-=1
                    break
        max_val = max(cnt, max_val)
        return
    for i in range(idx,len(letters)):
        storage.add(letters[i])
        combi(i+1,remain-1)
        storage.remove(letters[i])

N,K=map(int,input().split())
words=dict()
if K < 5:
    for _ in range(N):
        dummy = input()
    print(0)
else:
    basics=set() # 필수 글자 적어놓기
    for s in 'antic': 
        basics.add(s) 
    letters=set()
    for _ in range(N): # 단어들을 순회하며 필요한 글자를 저장
        word = str(input())[4:-4]
        words[word]=set()
        for w in word:
            if w not in basics: # 기본 글자가 아니라면 필요 글자에 추가
                words[word].add(w)
                letters.add(w)
    letters=list(letters)
    storage = set()
    max_val = 0
    # 가르쳐야 할 글자가 가르칠 수 있는 글자보다 적으면
    # 가르쳐야 할 글자들만큼만 확인
    K = min(len(letters)+5,K) 
    combi(0,K-5)
    print(max_val)
    # letters 리스트에 대한 K-5 개의 인덱스 조합을 구한 뒤 읽히는 최대 단어 수 갱신
