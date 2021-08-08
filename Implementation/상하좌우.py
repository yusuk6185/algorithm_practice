# N X N 크기의 정사각형 공간에서 여행가가 L, R, U, D 의 움직임을
# 명령받아 한 칸씩 이동한다. 도착할 지점의 좌표를 출력하는 프로그램을 작성.

n = int(input())

move = input().split()
row, col = 1, 1

for k in range(len(move)):
    if move[k] == 'R' and col < n:
        col += 1
    elif move[k] == 'L' and col > 1:
        col -= 1
    elif move[k] == 'U' and row > 1:
        row -= 1
    elif move[k] == 'D' and row < n:
        row += 1

print(row, col, end=' ')

