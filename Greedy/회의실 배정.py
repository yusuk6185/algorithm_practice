n = int(input())

meetings = []
for i in range(n):
    x, y = map(int, input().split())
    meetings.append((x, y))

meetings.sort(key = lambda x : x[0])
meetings.sort(key = lambda x : x[1])

time = 0
count = 0
for start, end in meetings:
    if start >= time:
        time = end
        count += 1

print(count)