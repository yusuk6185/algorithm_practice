n = int(input())
liquid = sorted(list(map(int, input().split())))

left, right = 0, n-1
answer = liquid[left] + liquid[right]
al = left
ar = right

while left < right:
    tmp = liquid[left] + liquid[right]
    if abs(tmp) < abs(answer):
        answer = tmp
        al = left
        ar = right
        if tmp == 0:
            break
    elif tmp < 0:
        left += 1
    else:
        right -= 1

print(liquid[al], liquid[ar])