S = input()
cArr = 0
chArr = 0
cheArr = 0
result = 0
for i in range(len(S)):
    if S[i] == 'C':
        cArr += 1
    elif S[i] == 'H' and cArr >= 1:
        chArr += 1
        cArr -= 1
    elif S[i] == 'E' and chArr >= 1:
        cheArr += 1
        chArr -= 1
    elif S[i] == 'F' and cheArr >= 1:
        result+=1
        cheArr -= 1
print(result)
