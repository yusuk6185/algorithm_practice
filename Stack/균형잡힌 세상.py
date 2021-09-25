# https://www.acmicpc.net/problem/4949

while True:
    s = input()
    if s == '.':
        break
    arr = []
    for i in s:
        arr.append(i)

    arr2 = []
    for i in arr:
        if i == '(':
            arr2.append('(')
        elif i == '[':
            arr2.append('[')
        elif i == ')':
            if len(arr2) > 0 and arr2[-1] == '(':
                arr2.pop()
            else:
                arr2.append(')'*100)
        elif i == ']':
            if len(arr2) > 0 and arr2[-1] == '[':
                arr2.pop()
            else:
                arr2.append(']'* 100)

    if len(arr2) == 0:
        print('yes')
    else:
        print('no')
 