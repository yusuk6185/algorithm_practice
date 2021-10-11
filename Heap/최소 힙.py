# https://www.acmicpc.net/problem/1927

import heapq
import sys

input = lambda : sys.stdin.readline().rstrip()

n = int(input())
heap = []

for i in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(heap, x)
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))