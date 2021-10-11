# https://www.acmicpc.net/problem/11279
import sys
import heapq

input = lambda : sys.stdin.readline().rstrip()

n = int(input())
heap = []

for i in range(n):
    x = int(input())
    if x:
        heapq.heappush(heap, (-x, x))
    else:
        if len(heap) >= 1:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
