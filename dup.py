n=2570
arr = []
result = 0
exc_res = 0
for i in range(1,n):
    arr.append(i)
dup = 1655
arr.append(dup)
for i in range(n):
    exc_res = exc_res^(i)
    result = result ^ arr[i]
print(result^exc_res)
