# https://www.acmicpc.net/problem/9461

dp = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16] + [0] * 100

def p(n):
    for i in range(10, n+1):
        dp[i] = dp[i-1] + dp[i-5]
    print(dp[n])
t = int(input())

for i in range(t):
    p(int(input()))