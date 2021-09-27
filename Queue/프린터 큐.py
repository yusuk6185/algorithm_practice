# https://www.acmicpc.net/problem/1966

from collections import deque

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    queue = deque()
    idx = deque()

    for i in arr:
        queue.append(i)
        idx.append(i)

    idx[m] = 'target'

    cnt = 1
    while True:
        if queue[0] == max(queue):
            queue.popleft()
            
            if idx[0] == 'target':
                print(cnt)
                break
            else:
                idx.popleft()
                cnt += 1

        else:
            queue.append(queue.popleft())
            idx.append(idx.popleft())