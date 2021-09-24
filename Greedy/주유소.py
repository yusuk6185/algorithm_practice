# https://www.acmicpc.net/problem/13305

n = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))

# 만약에 다음 도시의 기름값이 현재 도시의 기름값보다 비싸면 현재 도시에서
# 기름을 더넣고 반대의 경우 다음 도시까지 필요한 기름만 넣는다.

m = price[0]
cost = 0
for i in range(n-1):
    if m > price[i]:
        m = price[i]
    cost += m * road[i]

print(cost)