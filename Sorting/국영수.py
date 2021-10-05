import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
arr = []
for i in range(n):
    name, kor, eng, math = input().split()
    arr.append([name, int(kor), int(eng), int(math)])

arr.sort(key = lambda x : (-x[1], x[2], -x[3], x[0])) # -x[1] -> 국어 점수가 감소하는 순서, x[2] -> 국어 점수가 같으면 영어 점수가 증가하는 순서
for i in arr:
    print(i[0])