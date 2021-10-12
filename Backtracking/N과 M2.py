# https://www.acmicpc.net/problem/15650

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(1, n+1):
        if visited[i] == True:
            continue
        if s:
            if i < s[-1]:
                continue
        s.append(i)
        visited[i] = True
        dfs()
        s.pop()
        visited[i] = False

n, m = map(int, input().split())
s = []
visited = [False] * (n+1)

dfs()

