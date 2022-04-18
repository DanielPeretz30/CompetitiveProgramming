import math

dict = {}

def fact(n):
    if n == 1:
        return
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            if i in dict:
                dict[i] =  dict[i]+1
            else:
                dict[i] = 2
            fact(n//i)
            return
    if n in dict:
        dict[n] =  dict[n]+1
    else:
        dict[n] = 2



T = int(input())
for i in range(T):
    dict = {}
    n = int(input())
    A = list(map(int,input().split(" ")))
    for num in A:
        fact(num)
    result = 1
    for num in dict.values():
        result = result*num
    print(result)
