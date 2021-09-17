INF = int(1e9)

n = int(input())
a = [[INF] * (n+1) for _ in range(n+1)]

while True:
    s1, s2 = map(int, input().split())

    if s1 == -1 and s2 == -2:
        break
    a[s1][s2] = 1
    a[s2][s1] = 1

for i in range(1, n+1):
    a[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if a[i][j] == 1 or a[i][j] == 0:
                continue
            elif a[i][j] > a[i][k] + a[k][j]:
                a[i][j] = a[i][k] + a[k][j]

r = []
for i in range(1, n+1):
    r.append(max(a[i][1:]))

m = min(r)
print(m, r.count(m))
for i,v in enumerate(r):
    if v == m:
        print(i+1, end = ' ')