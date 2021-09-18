# https://www.acmicpc.net/problem/2869

a, b, v = map(int, input().split())

pre_move = (v-a)//(a-b)
remainder = (v-a)%(a-b)

if remainder == 0:
    print(pre_move+1)
else:
    print(pre_move+2)

# 시간 초과 문제를 해결하기 어려웠다.
# 뺄 수 있는 만큼 최대한 빼고 나머지를 갖고 계산했다.