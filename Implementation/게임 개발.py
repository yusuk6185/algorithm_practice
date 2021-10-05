# N X M 크기의 맵에서 캐릭터가 움직인다. 상하좌우로 움직일 수 있고, 바다로 되어
# 있는 공간에는 갈 수 없다.
#  
# 1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터
# 차례대로 갈 곳을 정한다. 
# 2. 캐릭터의 바로 왼쪽에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸을 전진한다. 왼쪽 방향에 가보지 않은
# 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.
# 3. 만약 네방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 바라보는 방향을
# 유지한 채로 한칸 뒤로 가고 1단계로 돌아간다. 이때 뒤쪽 방향이 바다라면 움직임을 멈춘다.

# 캐릭터가 방문한 칸의 수를 출력하는 프로그램을 만드시오.

n, m = map(int, input().split())

# create board with 0
board = [[0 for i in range(m)] for j in range(n)]

# take x, y axis and inital direction
x, y, d = map(int, input().split())

# take map information
for i in range(n):
    board[i] = list(map(int,input().split()))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# mark initial position as 1
board[x][y] = 1

def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

cnt = 1
turn_time = 0

while True:

    # turn left first
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]

    # if there is 0 in front of turned direction, move
    if board[nx][ny] == 0:
        board[nx][ny] = 1
        x, y = nx, ny
        cnt += 1
        turn_time = 0
        continue

    # if it is 1, turn left
    else:
        turn_time += 1

    # if there is no 0 in 4 directions
    if turn_time == 4:
        nx = x - dx[d]
        ny = x - dy[d]

        # move back 
        if board[nx][ny] == 0:
            x = nx
            y = ny
        # if it's 1, end
        else:
            break
        turn_time = 0

print(cnt)

# example input
# 4 4      N X M
# 1 1 0    x, y and direction
# 1 1 1 1  map
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1 

# example output
# 3