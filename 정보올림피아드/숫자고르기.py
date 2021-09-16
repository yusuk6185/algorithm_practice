# https://www.acmicpc.net/problem/2668

def dfs(v, i):
    visited[v] = True # 시작 노드를 방문처리

    for w in adj[v]: # 시작 노드에 담긴 숫자 노드 탐색 ex) 1 -> 3
        if not visited[w]: # 방문되지 않았다면 이동후 탐색 
            dfs(w, i)
        elif w == i: # 방문되었고 그 값이 i 와 같다면 결과값 추출
            result.append(i)

n = int(input())

adj = [[] for _ in range(n+1)] # 각 노드에 숫자 넣기
for i in range(n):
    adj[i+1].append(int(input()))

result = []

for i in range(1, n+1): # 각 노드를 돌 때마다 visited 리셋하고 dfs 실행
    visited = [False] * (n+1)
    dfs(i, i)

print(len(result))
for i in result:
    print(i)