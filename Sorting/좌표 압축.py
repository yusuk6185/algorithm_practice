# https://www.acmicpc.net/problem/18870

# 시간 초과 때문에 dic 자료형 사용해야 함. 사용법 숙지

import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
arr = list(map(int, input().split()))
arr2 = sorted(list(set(arr)))
dic = {arr2[i] : i for i in range(len(arr2))}

for i in arr:
    print(dic[i], end = ' ')