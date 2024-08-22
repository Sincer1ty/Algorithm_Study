N,K=map(int,input().split())
number_str=list(input())
number_int = list(map(int,number_str))
stack=[]
i=0
while  len(stack)<K:
    if number_int[i] < number_int[i+1]:
        a=number_int.pop(i)
        stack.append(a)
    elif number_int[i] == number_int[i+1]:
        i+=2
    else:
        a=number_int.pop(i+1)
        stack.append(a)
result="".join(map(str,number_int))
print(result)
