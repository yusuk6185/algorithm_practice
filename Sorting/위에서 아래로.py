# 하나의 수열에는 다양한 수가 존재한다. 이 수를 큰 수부터 작은 수의 순서로 정렬해야 한다.
# 수열을 내림차순으로 정렬하는 프로그램을 만드시오.

n = int(input())
result = []

for i in range(n):
    result.append(int(input()))

result = sorted(result, reverse=True)

for i in result:
    print(i, end = ' ')

# input example
# 3
# 15
# 27
# 12

# output example
# 27 15 12