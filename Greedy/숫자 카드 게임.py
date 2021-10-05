# n X m 형태의 카드 중 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임.
# 먼저 행을 선택하고 그 중에 가장 숫자가 낮은 카드를 뽑아야 한다.

n, m = map(int, input().split())

# create the card board.
board = [[0 for i in range(m)] for j in range(n)]
min_num = []

# fill out the card board and add the mininum number of each row to the list.
for i in range(n):
    board[i] = list(map(int, input().split()))
    min_num.append(min(board[i]))

# print the maximum number among the mininum number list.
print(max(min_num))

# input example
# 3 3
# 3 1 2
# 4 1 4
# 2 2 2

# output example
# 2