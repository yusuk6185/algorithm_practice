def dfs(v, i):
    visited[v] = True

    for w in adj[v]:
        if not visited[w]:
            dfs(w, i)
        elif w == i:
            result.append(i)

n = int(input())
adj = [[] for _ in range(n+1)]
for i in range(1, n+1):
    adj[i].append(int(input()))

result = []
for i in range(1, n+1):
    visited = [False] * (n + 1)
    dfs(i, i)

print(len(result))
for i in result:
    print(i)