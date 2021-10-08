# https://www.acmicpc.net/problem/1806

n, s = map(int, input().split())
array = list(map(int, input().split()))

left, right = 0, 0
answer = 100001
tmp_sum = 0

while True:
    if tmp_sum >= s:
        answer = min(answer, right - left)
        tmp_sum -= array[left]
        left += 1

    elif right == n:
        break

    else:
        tmp_sum += array[right]
        right += 1
    
if answer == 100001:
    print(0)
else:
    print(answer)