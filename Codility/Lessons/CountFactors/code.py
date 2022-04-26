import math

def solution(N):
    set = {1,N}
    if N == 1:
        return 1
    lim = int(math.sqrt(N))+1
    for i in range(2,lim):
        if N%i == 0:
            set.add(i)
            set.add(N//i)
    return len(set)
