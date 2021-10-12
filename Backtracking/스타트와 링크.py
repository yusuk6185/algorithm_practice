# https://www.acmicpc.net/problem/14889

import sys
sys.setrecursionlimit(10000)
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
arr = [list(map(int ,input().split())) for _ in range(n)]
visited = [0 for _ in range(n)]
ans = int(1e9)

def dfs(idx, cnt):
    global ans
    if cnt == n // 2:
        start, link = 0, 0

        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start += arr[i][j]
                elif not visited[i] and not visited[j]:
                    link += arr[i][j]
        
        ans = min(ans, abs(start - link))
    
    for i in range(idx, n):
        if visited[i]:
            continue

        visited[i] = 1
        dfs(i + 1, cnt + 1)
        visited[i] = 0

dfs(0, 0)
print(ans)