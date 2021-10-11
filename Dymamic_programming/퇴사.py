# https://www.acmicpc.net/problem/14501

import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())

table = [list(map(int, input().split())) for _ in range(n)]

dp = [0 for _ in range(n+1)]

for i in range(n-1, -1, -1):
    if i + table[i][0] > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(table[i][1] + dp[i + table[i][0]], dp[i+1])

print(dp[0])