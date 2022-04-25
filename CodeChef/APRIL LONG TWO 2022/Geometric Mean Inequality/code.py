import sys
input= sys.stdin.readline

T = int(input())
for j in range(T):
    N = int(input())
    x = input().split()
    pos = x.count('1')
    neg = x.count('-1')
    if abs(pos-neg) > 2:
        print("No")
    elif pos%2==0 and neg%2 == 0:
        if abs(pos - neg) <= 2:
            print("Yes")
        else:
            print("No")
    else:
        if abs(pos-neg) <=1:
            print("Yes")
        else:
            print("No")
