# https://www.acmicpc.net/problem/10866
import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

dq = deque()
n = int(input())
for _ in range(n):
    com, *num = input().split()
    if com == 'push_front':
        dq.appendleft(int(num[0]))
    elif com == 'push_back':
        dq.append(int(num[0]))
    elif com == 'pop_front':
        print(dq.popleft() if len(dq) != 0 else -1)
    elif com == 'pop_back':
        print(dq.pop() if len(dq) != 0 else -1)
    elif com == 'size':
        print(len(dq))
    elif com == 'empty':
        print(1 if len(dq) == 0 else 0)
    elif com == 'front':
        print(-1 if len(dq) == 0 else dq[0])
    elif com == 'back':
        print(-1 if len(dq) == 0 else dq[-1])