# 8 X 8 평면의 정원의 특정한 칸에 나이트가 서있다. 이동할 때는 L자 형태로만 이동
# 정원 밖으로는 나갈 수 없다. 2가지 경우로 이동한다.
# 1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동.
# 2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동.
# 나이트의 위치가 주어졌을 때 나이트가 이동 할 수 있는 경우의 수를 출력하는 프로그램을 작성.

# take input and convert it to integer
pos = input()
x, y = int(ord(pos[0]) - 96), int(pos[1])
cnt = 0

# move left horizontally
if x - 2 >= 1 and y - 1 >= 1:
    cnt += 1
if x - 2 >= 1 and y + 1 <= 8:
    cnt += 1
# move right horizontally
if x + 2 <= 8 and y - 1 >= 1:
    cnt += 1
if x + 2 <= 8 and y + 1 <= 8:
    cnt += 1
# move left perpendicularly
if x - 1 >= 1 and y - 2 >= 1:
    cnt += 1
if x - 1 >= 1 and y + 2 <= 8:
    cnt += 1
# move right perpendicularly
if x + 1 <= 8 and y - 2 >= 1:
    cnt += 1
if x + 1 <= 8 and y + 2 <= 8:
    cnt += 1

print(cnt)

# example input
# a1

# example output
# 2