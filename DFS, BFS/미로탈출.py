# N X M 크기의 직사각형 미로가 있다. 미로에는 괴물이 있어 이를 피해 탈출해야 한다.
# 시작 위치는 (1, 1)이고 미로의 출구는 (N, M)의 위치에 존재하며 한번에 한 칸씩
# 이동할 수 있다. 괴물이 있는 부분은 0, 없는 부분은 1로 표시되어 있다.
# 이때 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오.
from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        # check adjacent cells from current cell
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # continue if out of range or monster
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            # record shortest distance only if visiting new node
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # return shortest distance to right bottom cell
    return graph[n - 1][m - 1]

print(bfs(0, 0))

