# https://www.acmicpc.net/problem/1932

n = int(input())

d = [0 for _ in range(n+1)]

for i in range(n):
    d[i] = list(map(int, input().split()))

for i in range(1, n):
    for j in range(len(d[i])):
        if j == 0:
            d[i][j] = d[i][j] + d[i-1][j]
        elif j == len(d[i]) - 1:
            d[i][j] = d[i][j] + d[i-1][j-1]
        else:
            d[i][j] = d[i][j] + max(d[i-1][j-1], d[i-1][j])
    
print(max(d[n-1]))