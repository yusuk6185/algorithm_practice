dp = [0 for _ in range(301)]
arr = [0 for _ in range(301)]

n = int(input())

for i in range(n):
    arr[i] = int(input())

dp[0] = arr[0]
dp[1] = arr[0] + arr[1]

for i in range(2, n+1):
    dp[i] = max(dp[i-3] + arr[i-1] + arr[i], dp[i-2] + arr[i])

print(dp[n-1])

print(dp)