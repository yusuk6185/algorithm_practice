# https://www.acmicpc.net/problem/2108

# 최빈값 구할때 Counter 쓰는 거 숙지
# 문제 제대로 안읽어서 산술평균 소숫점 계산하는 거 때문에 여러번 틀림

import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())

result = []
for i in range(n):
    result.append(int(input()))

result.sort()
# 산술평균
print(round(sum(result) / n))

# 중앙값
print(result[n // 2])

# 최빈값
from collections import Counter
count = Counter(result).most_common(2)
if len(count) > 1 and count[0][1] == count[1][1]:
    print((count[1][0]))
else:
    print((count[0][0]))

# 범위
print(max(result) - min(result))
