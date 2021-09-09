# https://www.acmicpc.net/problem/1431

import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())

arr = [input() for i in range(n)]

def sum_num(serial):
    answer = 0
    for i in serial:
        if i.isdigit():
            answer += int(i)
    return answer

arr.sort(key = lambda x : (len(x), sum_num(x), x))

for i in arr:
    print(i)