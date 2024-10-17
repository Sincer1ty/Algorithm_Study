# K개까지의 단어를 가르칠 때, N개의 단어 중 몇 개를 읽을 수 있는가? 
import sys
read = sys.stdin.readline

n,k = map(int, read().strip().split())

tot_list = []
unique_char = set({'a','n','t','i','c'})

for i in range(n):
    alph_list = list(read().strip())
    tot_list.append(alph_list)

    alph_set = set(alph_list)
    
    # count+=1
    # print(count)
    
    if len(unique_char) < k:
        unique_char.update(alph_set)

    # # if len(unique_char) > k:
    # #     break
    # print(len(unique_char))
    
    # # save_unique_char = unique_char.copy()

# print(unique_char)

count=0
for i in range(n):
    word = set(tot_list[i][4:-4])

    if word.issubset(unique_char):
        count+=1

print(count)

# alph_list = list(map(str,read().strip().split()))

# print(unique_char)
# print(len(unique_char))

--------------------------------------------------------------------------------------------------------------

# K개까지의 단어를 가르칠 때, N개의 단어 중 몇 개를 읽을 수 있는가? 
import sys
read = sys.stdin.readline

n, k = map(int, read().split())

if k<5 :
    print(0)
    sys.exit()

elif k == 26: 
    print(n)
    sys.exit()

answer = 0
words = [set(read().strip()) for _ in range(n)]
base_chr = set('antic')

#base_chr에 들어 있는 글자를, alphabet중 어떤 것을 배웠는지를 표시하는 배열에 표기한다.
learn = [0] * 26
for chr in base_chr:
    learn[ord(chr) - ord('a')] = 1


#기본적인 글자 조합을 제외한, 전체 단어가 갖고 있는 글자의 조합을 저장한다.
all_chars = set()
for word in words:
    all_chars.update(word)
all_chars -=base_chr
all_chars = list(all_chars)


# idx 는 알파벳 상 순서, cnt는 배울 수 있는 총 글자의 개수를 의미한다
def dfs(idx, cnt):
    global answer 
    
    #cnt는 배울 수 있는 글자의 수를 난타낸다
    if cnt == k-5:
        read_cnt = 0
        for word in words:
            #learn배열에 단어 상 한 글자라도 안 들어가 있으면, check = False
            check = True
            for chr in word:
                if not learn[ord(chr) - ord('a')]:
                    check = False
                    break
            # learn 배열에 단어 상 모든 글자가 다 들어가 있으면, read_cnt +=1
            if check:
                read_cnt+=1

        answer = max(answer, read_cnt)
        return

    # # 알파벳 상 모든 글자를 하나씩 배우면서, 어떤 글자를 학습했을 때 가장 많은 단어를 이해할 수 있는지 확인한다.
    # for i in range(idx, 26):
    #     if not learn[i]:
    #         learn[i] = True
    #         dfs(i+1, cnt+1)
    #         learn[i] = False

    # 전체 단어에서 갖고 있는 글자 조합에서만 글자를 하나씩 배우면서, 어떤 글자를 학습했을 때 가장 많은 단어를 이해할 수 있는지 확인한다.
    for i in range(idx, len(all_chars)):
        char_idx = ord(all_chars[i]) - ord('a')
        if not learn[char_idx]:
            # 전체 단어에서 갖고 있는 글자 조합 중 하나의 글자를 배웠을 시, 학습할 수 있는 단어의 개수를 구한다.
            learn[char_idx] = 1
            dfs(i+1, cnt+1)
            # 전체 단어에서 갖고 있는 글자 조합 중 하나의 글자를 다시 안 배우고, 다른 글자를 배웠을 때 학습할 수 있는 단어의 개수를 구한다.
            learn[char_idx] = 0



dfs(0,0)
print(answer)



