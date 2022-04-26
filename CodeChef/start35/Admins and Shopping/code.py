import sys
import math
input= sys.stdin.readline

T = int(input())
for j in range(T):
    N,X = map(int,input().split())
    A_i = list(set(map(int,input().split())))
    ai = min(A_i)
    r = math.ceil(X/ai)
    print(max(N,r))
