# https://www.acmicpc.net/problem/11729

n = int(input())

def hanoi(n, start, mid, end): # 봉은 세 개
    if n == 1: # 원판이 하나라면 한번에 끝
        move.append([start, end])
    else:
        hanoi(n-1, start, end, mid) # 제일 큰 원반을 제외한 원반들을 mid 로 옮긴다
        move.append([start, end]) # 제일 큰 원반을 목표 봉으로 옮긴다
        hanoi(n-1, mid, start, end) # 나머지 봉들을 목표 봉으로 옮긴다

move = []

hanoi(n, 1, 2, 3)
print(len(move))
for a, b  in move:
    print(a, b, end = ' ')
    print()