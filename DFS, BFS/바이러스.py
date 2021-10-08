# https://www.acmicpc.net/problem/2606

def dfs(v):
    global count
    visited[v] = 1
    for i in range(1, n+1):
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(i)
            count += 1

n = int(input())
m = int(input())
graph = [[0] * (n+1) for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

visited = [0] * (n+1)
count = 0

dfs(1)
print(count)