# https://www.acmicpc.net/problem/2659

def find_clock_num(num):
    clock_num = num
    for _ in range(3):
        num = (num % 1000) * 10 + num // 1000
        if clock_num > num:
            clock_num = num
    return clock_num

num = int(''.join(input().split()))
clock_num = find_clock_num(num)

i = 1111
count = 0
while (i <= clock_num):
    if i == find_clock_num(i):
        count += 1
    i += 1
    
print(count)
