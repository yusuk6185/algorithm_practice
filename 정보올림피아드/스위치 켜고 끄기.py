# https://www.acmicpc.net/problem/1244

# 구현, 시뮬레이션

def turn(num):
    if switch[num] == 1:
        switch[num] = 0
    elif switch[num] == 0:
        switch[num] = 1

n = int(input())
switch = [0] + list(map(int, input().split()))
stu_num = int(input())

for _ in range(stu_num):
    gen, num = map(int,input().split())
    if gen == 1:
        for i in range(1, n+1):
            if i % num == 0:
                turn(i)
    elif gen == 2:
        turn(num)
        j = 1
        while True:
            if num-j < 1 or num + j > n:
                break
            if switch[num-j] == switch[num+j]:
                turn(num-j)
                turn(num+j)
            else: break
            j += 1

for i in range(1, n+1):
    print(switch[i], end = ' ')
    if i % 20 == 0:
        print()
