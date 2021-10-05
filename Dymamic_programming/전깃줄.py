# https://www.acmicpc.net/problem/2565

n = int(input())
arr = [[0] for _ in range(n)]

for i in range(n):
    arr[i]=list(map(int, input().split()))

arr.sort()
dp = [1 for _ in range(501)]

for i in range(n):
    for j in range(i):
        if arr[i][1] > arr[j][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))