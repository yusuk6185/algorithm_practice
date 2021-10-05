# N이 1이 될 때까지 N에서 1을 빼거나 N이 K로 나누어떨어질 때는 N을 K로 나눈다.

n, k = map(int,input().split())
cnt = 0

while True:
    if n == 1:
        break
    if n % k == 0:
        n //= k
        cnt += 1
    else:
        n -= 1
        cnt += 1

print(cnt)

# input example
# 25 5

# output example
# 2