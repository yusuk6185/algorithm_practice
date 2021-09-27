# https://www.acmicpc.net/problem/1021

from collections import deque

n, m = map(int, input().split())
pos = list(map(int, input().split()))
queue = deque([i for i in range(1, n+1)])

count = 0
for i in pos:
    while True:
        if queue[0] == i:
            queue.popleft()
            break
        else:
            if queue.index(i) < len(queue)/2:
                while queue[0] != i:
                    queue.append(queue.popleft())
                    count += 1
            else:
                while queue[0] != i:
                    queue.appendleft(queue.pop())
                    count += 1

print(count)