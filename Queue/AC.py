# https://www.acmicpc.net/problem/5430

from collections import deque
import sys

input = lambda: sys.stdin.readline().rstrip()

t = int(input())

for i in range(t):
    cmd = input()
    n = int(input())
    temp = True

    nums = input()[1:-1].split(',')
    queue = deque()
    for j in nums:
        if j.isdigit():
            queue.append(int(j))
    reverse = 0

    for k in cmd:
        if k == 'R':
            if reverse == 0:
                reverse = 1
            else:
                reverse = 0
        elif k == 'D':
            if queue and queue[0] != '':
                if reverse == 0:
                    queue.popleft()
                else:
                    queue.pop()
            else:
                temp = False
                break
                
    if temp == False:
        print('error')

    else:
        if reverse == 1:
            queue.reverse()

        print("[", end='')
        for i in range(len(queue)):
            if i == len(queue)-1:
                print(queue[i],end='')
            else:
                print(queue[i],end=',')
        print("]")
