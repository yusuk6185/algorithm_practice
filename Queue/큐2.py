# https://www.acmicpc.net/problem/18258

# DEQUE 안쓰고 푸는 법

# import sys
# input = lambda : sys.stdin.readline().rstrip()

# n = int(input())
# queue = []

# cnt = 0
# for i in range(n):
#     cmd, *num = input().split()
#     if cmd == 'push':
#         queue.append(int(num[0]))
#     elif cmd == 'pop':
#         if len(queue) - cnt == 0:
#             print(-1)
#         else:
#             print(queue[cnt])
#             cnt += 1
#     elif cmd == 'size':
#         print(len(queue) - cnt)
#     elif cmd == 'empty':
#         print(1 if len(queue)-cnt == 0 else 0)
#     elif cmd == 'front':
#         print(-1 if len(queue) - cnt == 0 else queue[cnt])
#     elif cmd == 'back':
#         print(-1 if len(queue) - cnt == 0 else queue[-1])

from collections import deque
import sys

input = lambda : sys.stdin.readline().rstrip()

n = int(input())
queue = deque()

for i in range(n):
    cmd, *num = input().split()
    if cmd == 'push':
        queue.append(int(num[0]))
    elif cmd == 'pop':
        print(queue.popleft() if len(queue) > 0 else -1)
    elif cmd == 'size':
        print(len(queue) if len(queue) > 0 else 0)
    elif cmd == 'empty':
        print(1 if len(queue) == 0 else 0)
    elif cmd == 'front':
        print(queue[0] if len(queue) > 0 else -1)
    elif cmd == 'back':
        print(queue[-1] if len(queue) > 0 else -1) 