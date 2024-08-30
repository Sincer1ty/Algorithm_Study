import sys
input = sys.stdin.readline

# 수의 개수
N = int(input())

number = list(map(int, input().split()))

# +, -, x, / 의 개수
opNum= list(map(int, input().split()))

op = []
for i, o in enumerate(opNum):
    for _ in range(o):
        op.append(i)

perms = []
temp = []
def permute(arr, temp):
    if not arr:
        perms.append(temp)
        return temp[:-1]
    
    for i in range(len(arr)):
        temp.append(arr[i])
        temp = permute(arr[:i]+arr[i+1:], temp)
    
    return temp[:-1]

permute(op, temp)

can = []
for p in perms:
    for i, n in enumerate(number):
        if i == 0:
            result = number[0]
            continue
        if p[i-1] == 0:
            result += n
        elif p[i-1] == 1:
            result -= n
        elif p[i-1] == 2:
            result *= n
        elif p[i-1] == 3:
            if result < 0 :
                result = (-1*result // n) * -1
            else:
                result //= n
    can.append(result)

print(max(can))
print(min(can))
