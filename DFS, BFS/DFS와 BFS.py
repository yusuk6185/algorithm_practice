# https://www.acmicpc.net/problem/1260

from collections import deque

def dfs(v):
    visited[v] = 1
    print(v, end = ' ')
    for i in range(1, n+1):
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(i)

def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = 1

    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in range(1, n+1):
            if graph[v][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = 1

n, m, v = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

visited = [0] * (n+1)

dfs(v)
visited = [0] * (n+1)
print()
bfs(v)