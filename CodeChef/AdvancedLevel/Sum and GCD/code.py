import math
T = int(input())
for j in range(T):
    n = int(input())
    A = list(set(map(int,input().split())))
    A.sort()
    n_1 = len(A)
    if n_1==1:
        print(2*A[0])
    elif n_1==2:
        print(A[0]+A[1])
    else:
        gcd_a = A[-1]
        gcd_b = A[-2]
        gcd_c = 0
        for i in range(0,n_1-2):
            gcd_c = math.gcd(gcd_c,A[i])
        op1 = gcd_a + math.gcd(gcd_c,gcd_b)
        op2 = gcd_b + math.gcd(gcd_c,gcd_a)
        print(max(op1,op2))
