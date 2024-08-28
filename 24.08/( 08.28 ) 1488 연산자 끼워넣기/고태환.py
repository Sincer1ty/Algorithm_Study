def backtrack(num, idx, p, m, mt, dv):
    global min_val, max_val
    idx += 1
    if idx == N:
        min_val = min(min_val, num)
        max_val = max(max_val, num)
        return
  
    next_num = arr[idx]
    if p != 0:
        backtrack(num + next_num, idx, p - 1, m, mt, dv)
    if m != 0:
        backtrack(num - next_num, idx, p, m - 1, mt, dv)
    if mt != 0:
        backtrack(num * next_num, idx, p, m, mt - 1, dv)
    if dv != 0:
        if num < 0:
            backtrack(-(abs(num) // next_num), idx, p, m, mt, dv - 1)
        else:
            backtrack(num // next_num, idx, p, m, mt, dv - 1)
        
N = int(input())
arr = list(map(int, input().split()))
ope = list(map(int, input().split()))
idx = 0
num = arr[idx]
min_val, max_val = float('inf'), -float('inf')
backtrack(num, idx, ope[0], ope[1], ope[2], ope[3])
print(max_val)
print(min_val)