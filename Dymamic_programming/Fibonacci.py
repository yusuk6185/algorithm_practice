d = [0] * 101

d[1] = 1
d[2] = 1
n = 100

for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]

for i in range(1, 51):
    print(d[i], end = ' ')