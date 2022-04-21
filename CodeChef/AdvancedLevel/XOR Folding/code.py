import sys

input= sys.stdin.readline
T = int(input())
for j in range(T):
    x,y = map(int,input().split())
    counter = 0
    for i in range(x):
        A = input()
        if A.count("1")%2:
            counter += 1
    if counter%2 == 0:
        print("NO")
    else:
        print("YES")
