# https://www.acmicpc.net/problem/2751

import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())

arr = [int(input()) for i in range(n)]

arr.sort()

for i in arr:
    print(arr)