# 정수 X가 주어질 때 사용할 수 있는 연산은 다음 4가지이다.
# 1. X가 5로 나누어 떨어지면, 5로 나눈다.
# 2. X가 3으로 나누어 떨어지면, 3으로 나눈다.
# 3. X가 2로 나누어떨어지면, 2로 나눈다.
# 4. X에서 1을 뺀다.
# 연산 4개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

x = int(input())

# initiate dynamic programming table
d = [0] * 30001

for i in range(2, x + 1):
    # if i cannot be divided by 2, 3, 5, it must be subtracted by 1.
    d[i] = d[i - 1] + 1
    # if i can be divided by 2, select minimum value between subtracting 1 or dividing by 2.
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    # same for 3 and 5
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)

print(d[x])