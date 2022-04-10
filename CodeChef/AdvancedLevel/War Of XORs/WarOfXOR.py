


T = int(input())
for i in range(T):
    n = int(input())
    A = list(map(int,input().split(" ")))
    odd = []
    even = []
    for item in A:
        if item%2 == 1:
            odd.append(item)
        else:
            even.append(item)
    odd.sort()
    even.sort()
    counter = 0
    i = 0
    while( i < len(odd)):
        j = 0
        q = 0
        while(i < len(odd)-1 and odd[i] == odd[i+1]):
            i = i + 1
            q = q + 1
        while(i+j+1 < len(odd) and odd[i]^odd[i+j+1]==2):
            j = j+1
        counter = counter + (q + 1)*(len(odd)-(i+j+1))
        i = i+1
    i = 0
    while( i < len(even)):
        j = 0
        q = 0
        while(i <len(even)-1 and even[i] == even[i+1]):
            i = i + 1
            q = q + 1
        while(i+j+1 < len(even) and even[i]^even[i+j+1]==2):
            j = j+1
        counter = counter + (q + 1)*(len(even)-(i+j+1))
        i = i+1
    print(counter)