# https://www.acmicpc.net/problem/1874

n = int(input())

count = 1
stack = []
result = []
temp = True
for i in range(n):
    num = int(input())
    while count <= num:
        stack.append(count)
        result.append('+')
        count += 1
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        temp = False

if temp == False:
    print('NO')
else:
    for i in result:
        print(i)