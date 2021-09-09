# https://www.acmicpc.net/problem/11946

from typing import Mapping


n, m, q = map(int,input().split())

arr = [[] for _ in range(m)]

# 문제 번호 별로 나누기
for i in range(q):
    time, team, question, result = input().split()
    arr[int(question) - 1].append([int(time), int(team), result])


total = [[] for i in range(n)]
count = [[] for i in range(n)]
wrong = ['RE', 'TLE', 'WA']
for question in arr:
    for record in question:
        if record[2] == 'AC':
            total[record[1]].append(record[0])
            count += 1
            break


        


# 그 배열에서 sorting 함