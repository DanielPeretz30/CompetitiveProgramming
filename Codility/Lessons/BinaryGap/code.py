def solution(N):
    if N == 0:
        return 0
    result = 0
    cont = 0
    for i in bin(N)[3:]:
        if i == '0':
            cont += 1
        else:
            result = max(result,cont)
            cont = 0
    return result
