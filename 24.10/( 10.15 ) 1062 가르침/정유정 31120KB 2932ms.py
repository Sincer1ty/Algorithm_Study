import sys
sys.setrecursionlimit(1000000)

words_num, alphabet_num = map(int, sys.stdin.readline().strip().split())

if alphabet_num < 5:
    print(0)
    exit()

if alphabet_num == 26:
    print(words_num)
    exit()

# words = [list(input().rstrip()) for _ in range(words_num)]
words = []
for i in range(words_num):
    word = sys.stdin.readline().strip()
    words.append(set(word) - set('antic'))

legible_alpha = [0] * 26

for w in ('a', 'n', 't', 'i', 'c'):
    legible_alpha[ord(w) - ord('a')] = True

answer = 0


def dfs(idx: int, cnt: int) -> None:
    global answer

    if cnt == alphabet_num - 5:
        read_cnt = 0
        for word in words:
            flag = True

            for w in word:
                if not legible_alpha[ord(w) - ord('a')]:
                    flag = False
                    break

            if flag:
                read_cnt += 1

        answer = max(answer, read_cnt)
        return

    for i in range(idx, 26):
        if not legible_alpha[i]:
            legible_alpha[i] = True
            dfs(i, cnt + 1)
            legible_alpha[i] = False


dfs(0, 0)
print(answer)
