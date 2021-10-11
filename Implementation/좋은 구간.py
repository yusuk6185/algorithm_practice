# https://www.acmicpc.net/problem/1059

import sys
input = lambda : sys.stdin.readline().rstrip()

l = int(input())
s = list(map(int, input().split()))
n = int(input())

s.sort()

left = 0
right = 0
if n in s:
    print(0)
else:
    for x in s:
        if n > x:
            left = x+1
        else:
            right = x-1
            break

print(left, right)