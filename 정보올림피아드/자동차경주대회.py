# https://www.acmicpc.net/problem/2651

# 최대 거리를 넘지 않는 선에서 정비소를 들린다.
# 그 조합 중에서 정비 시간의 합이 가장 적은 조합을 선택

L = int(input())
N = int(input())
A = [0] * (N+2)
a = list(map(int, input().split()))
for i in range(1, N+2): A[i] += A[i-1] + a[i-1]
T = [0] + list(map(int, input().split())) + [0]
D = [int(1e9)] * (N+2)
C = [0] * (N+2)
R = [[] for _ in range(N+2)]
D[0] = 0
for i in range(1, N+2):
    for j in range(i - 1, -1, -1):
        if A[i]-A[j]<= L and D[j] + T[i] < D[i]:
            D[i] = D[j] + T[i]
            C[i] = C[j] + 1
            R[i] = R[j] + [str(i)]

print(D[-1])
print(C[-1]-1)
print(' '.join(R[-1][:-1]))