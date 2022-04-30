import bisect

def checkSol(Sol,K,A):
    n = len(A)
    index = 0
    M = Sol
    i = 0
    while K>0:
        i += 1
        K = K-1
        index = bisect.bisect(A,Sol)
        Sol = M + A[index-1]
        if index >= n:
            return 1
    if index < n:
        return -1
    return 1

def solution(K,M,A):
    n = len(A)
    sumArr = [0]*n
    sum = 0
    maxElm = 0
    for i in range(n):
        maxElm = max(maxElm,A[i])
        sum += A[i]
        sumArr[i] = sum
    #solution range is [maxElm,sum]
    if K == 1:
        return sum
    if K == n:
        return maxElm
    a = maxElm
    b = sum
    result = 0
    while a<=b:
        mid = (a+b)//2
        if checkSol(mid,K,sumArr) == 1:
            b = mid-1
            result = mid
        else:
            a = mid+1
    return result
