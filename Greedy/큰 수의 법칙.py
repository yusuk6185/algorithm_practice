# 배열에서 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙.
# 특정 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없다.

n, m, k = map(int, input().split())
num = list(map(int, input().split()))

sum = 0
num.sort() 

if num[-1] == num[-2]:
    for i in range(m):
        sum += num[-1]
else:
    for i in range(m):
    # m 번째 차례마다 두번째로 큰 수를 더함
        if i != 0 and (i+1) % (k+1) == 0:
            sum += num[-2]
        else:
            sum += num[-1] 

print(sum)

# 입력 예시
# 5 8 3
# 2 4 5 4 6

# 출력 예시
# 46