# https://www.acmicpc.net/problem/2178

from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if board[nx][ny] == 0:
                continue
            if board[nx][ny] == 1:
                board[nx][ny] = board[x][y] + 1
                queue.append((nx, ny))
        # for i in range(n):
        #     for j in range(m):
        #         print(board[i][j], end = ' ')
        #     print()
        # print()
    
    return board[n-1][m-1]


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m = map(int, input().split())
board = []

for i in range(n):
    board.append(list(map(int, input())))

print(bfs(0, 0))