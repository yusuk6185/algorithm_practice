# https://www.acmicpc.net/problem/3273

n = int(input())
array = sorted(list(map(int, input().split())))
x = int(input())

start, end = 0, n-1
answer = 0

while start < end:
    tmp = array[start] + array[end]
    if tmp == x:
        answer += 1
        start += 1
    elif tmp < x:
        start += 1
    else:
        end -= 1

print(answer)