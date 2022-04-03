n=257
arr = []
result = 0
exc_res = 0
for i in range(1,n):
    arr.append(i)
dup = 16
arr.append(dup)
for i in range(n-1):
    exc_res = exc_res^(i+1)
    result = result ^ arr[i]
result = result ^ arr[n-1]
print(result^exc_res)