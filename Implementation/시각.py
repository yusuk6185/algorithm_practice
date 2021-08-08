# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이
# 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오.

n = int(input())
cnt = 0

for k in range(0, n+1):
    for i in range(0, 60):
        for j in range(0, 60):
            if '3' in (str(k) + str(i) + str(j)):
                cnt += 1

print(cnt)