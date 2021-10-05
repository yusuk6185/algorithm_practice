# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이
# 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오.

n = int(input())
cnt = 0

# create nested for loops for hour, minute, and second.
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            # convert to str and combine them to find numbber 3 in it.
            if '3' in str(h) + str(m) + str(s):
                cnt += 1

print(cnt)

# example input
# 5

# example output
# 11475