# https://www.acmicpc.net/problem/1012
import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return
    if board[x][y] == 0:
        return

    board[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        dfs(nx, ny)

t = int(input())
answer = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for test in range(t):
    m, n, k = map(int, input().split())
    board = [[0] * m for _ in range(n)]

    for i in range(k):
        y, x = map(int, input().split())
        board[x][y] = 1

    count = 0

    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                dfs(i, j)
                count += 1

    answer.append(count)

for i in answer:
    print(i)