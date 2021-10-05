# https://www.acmicpc.net/problem/17298

n = int(input())
arr = list(map(int, input().split()))

stack = []
answer = [-1] * n
for i in range(n):
    while stack and arr[stack[-1]] < arr[i]:
        answer[stack.pop()] = arr[i]
    stack.append(i)

print(*answer)


# 스택은 값이 아닌 '인덱스'를 저장
# 오큰수가 없으면 -1을 출력해야 하므로 정답 배열 answer을 -1로 초기화
# 입력받은 수들 배열 arr을 탐색

# stack이 비어있지 않고, arr[스택 맨위]가 arr[i]보다 작으면 반복
# answer의 stack.pop()한 인덱스 자리에 arr[i]를 넣는다.
# stack에 i를 넣는다.