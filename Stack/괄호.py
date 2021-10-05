# https://www.acmicpc.net/problem/9012

t = int(input())

for i in range(t):
    string = list(input())
    result = []
    for j in string:
        if j == '(':
            result.append('(')
        elif j == ')':
            if len(result) == 0:
                result.append('('*100)
                break
            else:
                result.pop()
    if len(result) > 0:
        print('NO')
    else:
        print('YES')