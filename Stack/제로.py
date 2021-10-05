# https://www.acmicpc.net/problem/10773

k = int(input())
book = []

for i in range(k):
    num = int(input())
    if num != 0:
        book.append(num)
    else:
        book.pop()

print(sum(book))