T = int(input())
for i in range(T):
    n1 = int(input())
    A = list(map(int,input().split(" ")))
    lis = []
    lis.append(A[0])
    for i in range(1,n1):
        n = len(lis)
        find = A[i]
        if lis[n-1] <= find:
            lis.append(A[i])
        else:
            left = 0
            right = n
            flag = 1
            while(flag):
                middle = (left+right)//2
                if find < lis[middle] and find >= lis[middle-1]:
                    flag = 0
                elif find < lis[middle]:
                    right = middle
                else:
                    left = middle
                if left == right:
                    flag = 0
            lis[middle] = find
    print(len(lis),*lis)
