import sys
read = sys.stdin.readline

up, down, h = map(int,read().strip().split())

# ud_list = [up, down]
# sum = 0
# day = 0

# while sum < h:
#     for i in range(2):
#         if i%2==0:
#             sum+= ud_list[i]

#             if sum >= h:
#                 break
#         else:
#             sum-= ud_list[i]
#     print(sum)
#     day+=1

# print(day)

if (h - down) % (up-down) ==0:
    print ((h-down) // (up-down))
else:
    print ((h-down) // (up-down) +1)




