







def bestSecond(A,n):
    best = 0
    second = 0
    counter = 0
    for i in range(n):
        if A[i] == 0:
            counter += 1
        else:
            if counter > best:
                second = best
                best = counter
            elif counter == best:
                second = counter
            elif counter > second:
                second = counter
            counter = 0
    return best,second



T = int(input())
for i in range(T):
    n = int(input())
    A =list(map(int,input().split(" ")))
    best , second = bestSecond(A,n)
    eh = 0
    if best%2 == 0:
        eh = best/2
    else:
        eh = 1+(best//2)
    if best == second == 0:
        print('No')
    elif second >= eh:
        print('No')
    elif best%2 == 0:
        print('No')
    else:
        print("Yes")
