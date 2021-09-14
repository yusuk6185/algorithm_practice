# https://www.acmicpc.net/problem/2669

# 모든 x, y 좌표는 1이상 100이하인 정수기 때문에 100 X 100 크기의 보드를 만듬
board = [[0 for _ in range(101)] for j in range(101)]

# 4개의 정사각형 정보를 입력받고 해당하는 위치를 1로 바꿈
for i in range(4):
    x_l, y_l, x_r, y_r = map(int,input().split())
    for j in range(x_l, x_r):
        for k in range(y_l, y_r):
            board[j][k] = 1

# 보드위의 1의 개수를 셈
count = 0    
for i in range(101):
    for j in range(101):
        if board[i][j] == 1:
            count += 1

print(count)