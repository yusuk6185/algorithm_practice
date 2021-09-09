# https://www.acmicpc.net/problem/10814

import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())

arr = []
for i in range(n):
    age, name = input().split()
    arr.append([int(age), name])

arr.sort(key = lambda x : x[0])
for i in arr:
    print(i[0], i[1])