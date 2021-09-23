# https://www.acmicpc.net/problem/10989

import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
result = [0] * 10001

for i in range(n):
    num = int(input())
    result[num] += 1

for i in range(10001):
    if result[i] != 0:
        for j in range(result[i]):
            print(i)