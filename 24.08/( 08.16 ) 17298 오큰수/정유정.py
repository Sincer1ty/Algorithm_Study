import sys

size = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))
nge_arr = [-1] * size

for i in range(1, size):

# while idx < size:
#     right = idx + 1
#     for right in range(right, size):
#         if arr[right] > arr[idx]:
#             nge_arr[idx] = arr[right]
#             break
#
#     idx += 1
#
# for i in range(size):
#     sys.stdout.write(str(nge_arr[i]) + " ")
