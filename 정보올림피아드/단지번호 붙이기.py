# https://www.acmicpc.net/problem/2667

#BFS
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(graph, a, b):
    # 큐를 활성화 하고 시작점으로 a, b 좌표를 넣는다.
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0 # (a, b)를 0 으로 바꾸고 카운트를 센다
    count = 1

    while queue: # 큐가 빌 때까지 반복
        x, y = queue.popleft() # 큐의 첫번째 항목을 꺼낸다.
        for i in range(4): # 상하좌우를 확인
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n: # 범위에서 벗어나면 무시
                continue
            if graph[nx][ny] == 1: # 만약에 상하좌우에서 탐색할 노드가 발견되면
                graph[nx][ny] = 0 # 좌표의 값을 0 으로 바꾸고 큐에 추가함
                queue.append((nx, ny))
                count += 1 # 카운트 추가
    return count

n = int(input())
graph = []
for i in range(n): # 그래프에 입력값 담기
    graph.append(list(map(int, input())))

cnt = []
for i in range(n): # 그래프의 모든 노드 중에
    for j in range(n):
        if graph[i][j] == 1: # 탐색 시작할 노드가 발견되면 bfs 함수 호출
            cnt.append(bfs(graph, i, j))

cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])

# DFS SOLUTION
n = int(input())
graph = []
num = []

for i in range(n):
    graph.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    if 0 <= x < n and 0 <= y < n:
        if graph[x][y] == 1:
            global count
            count += 1
            graph[x][y] = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                dfs(nx, ny)
            return True
    return False

count = 0 
result = 0

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            num.append(count)
            result += 1
            count = 0

num.sort()
print(result)
for i in num:
    print(i)