# https://www.acmicpc.net/problem/2660

# 플루이드 워셜 알고리즘 사용 (최단 거리 계산)

INF = int(1e9)

n = int(input())
# 친구 관계 초기화
friend = [[INF] * (n+1) for _ in range(n+1)]

# s1, s2 = -1, -1 이 입력될 때까지 새로운 관계 입력
while True:
    s1, s2 = map(int, input().split())

    if s1 == -1 and s2 == -1:
        break
    friend[s1][s2] = 1
    friend[s2][s1] = 1

# 스스로에 대한 관계는 0으로 처리
for i in range(1, n+1):
    friend[i][i] = 0

# 플루이드 워셜 알고리즘 적용
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            # 친구를 거쳐서 가는 거리가 더 가깝다면 갱신
            if friend[i][j] == 1 or friend[i][j] == 0:
                continue
            elif friend[i][j] > friend[i][k] + friend[k][j]:
                friend[i][j] = friend[i][k] + friend[k][j]

# 회원의 모든 관계 중 제일 큰 값을 구한다 -> 각 회원의 점수
point = []
for i in range(1, n+1):
    point.append(max(friend[i][1:]))

# 모든 회원 중에 점수가 제일 낮은 사람이 회장 -> 제일 점수가 작은 사람을 찾는다
m = min(point)
print(m, point.count(m))

for i,v in enumerate(point):
    if v == m:
        print(i+1, end = ' ')