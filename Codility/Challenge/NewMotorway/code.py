import math
def solution(A):
    mod = int(math.pow(10,9))+7
    n = len(A)
    maxSave = 0
    index = n-1
    for i in range(n):
        can = (i+1)*(A[-1]-A[i])
        if can > maxSave:
            maxSave = can
            index = i
    result = 0
    for i in range(index):
        result += A[index]-A[i]
    for i in range(index+1,n):
        result += A[-1]-A[i]
    result = result%mod
    return result
