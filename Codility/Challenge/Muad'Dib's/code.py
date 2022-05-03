import bisect
def solution(A):
    A.insert(0,0)
    n = len(A)
    dp = [0]*n
    for i in range(1,n):
        op1 = dp[i-1] + 2
        index = bisect.bisect(A,A[i]-7)
        op2 = dp[index-1] + 7
        index = bisect.bisect(A,A[i]-30)
        op3 = dp[index-1] + 25
        dp[i] = min(op1,op2,op3)
    return dp[n-1]
