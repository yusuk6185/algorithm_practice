# https://www.acmicpc.net/problem/1654

k, n = map(int, input().split())
lines = [int(input()) for _ in range(k)]

start, end = 1, max(lines)

while start <= end:
    mid = (start + end) // 2
    total = 0
    
    for line in lines:
        total += line // mid
    
    if total >= n:
        start = mid + 1
        answer = mid

    else:
        end = mid - 1

print(answer)