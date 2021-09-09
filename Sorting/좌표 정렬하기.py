# https://www.acmicpc.net/problem/11650

import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())

arr = []
for i in range(n):
    x, y = map(int, input().split())
    arr.append([x, y])

arr.sort(key = lambda x : (x[0], x[1]))

for i in arr:
    print(i[0], i[1])