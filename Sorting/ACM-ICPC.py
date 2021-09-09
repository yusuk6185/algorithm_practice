# https://www.acmicpc.net/problem/11946

import sys
input = lambda : sys.stdin.readline().rstrip()

n, m, q = map(int,input().split())

arr = [[[301, 0] for _ in range(m + 1)] for _ in range(n + 1)] #[정답 시간, 오답 페널티]

for _ in range(q):
    time, team, prob, result = input().split()
    time = int(time)
    team = int(team)
    prob = int(prob)

    if arr[team][prob][0] == 301: # 아직 못 맞혔을 경우
        if result == 'AC':
            arr[team][prob][0] = time # 최소 정답 시간
        else:
            arr[team][prob][1] += 20 # 오답 페널티

grade = [[i, 0, 0] for i in range(n + 1)] # [팀 번호, 푼 문제, 총 시간]

for team in range(1, n+1):
    for prob in range(1, m+1):
        if arr[team][prob][0] != 301:
            grade[team][1] += 1 # 문제 개수
            grade[team][2] += arr[team][prob][0] # 정답 시간
            grade[team][2] += arr[team][prob][1] # 오답 패널티

grade = sorted(grade[1:], key = lambda x : (-x[1], x[2], x[0])) # 순서대로 정렬

for i in grade:
    print(i[0], i[1], i[2])