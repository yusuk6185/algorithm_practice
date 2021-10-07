# https://www.acmicpc.net/problem/2470

n = int(input())
liquid = sorted(list(map(int, input().split())))

left, right = 0, n-1
al = left
ar = right
mini = liquid[left] + liquid[right]

while left < right:
    tmp = liquid[left] + liquid[right]
    if abs(tmp) < abs(mini):
        mini = tmp
        al = left
        ar = right
        if tmp == 0:
            break

    if tmp < 0:
        left += 1
    
    else:
        right -= 1

print(liquid[al], liquid[ar])