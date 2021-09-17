# https://www.acmicpc.net/problem/2635

# 브루트 포스

N = int(input())

max_l = 0
max_list = []

# 두 번째 수를 결정하기
for i in range(N+1):
    result = [N, i] # 첫번째, 두번째 수
    j = 0
    while(True):
        new_num = result[j] - result[j+1] # 다음수는 first - second
        if new_num <= -1: # 다음 수가 음수라면 루프 탈출
            break
        result.append(new_num) # 아니면 이어가기 리스트에 추가
        if max_l < len(result): # 기존 second 보다 새로운 second 가 더 많은 수를 만든다면
            max_l = len(result) # max list 갱신
            max_list = result
        j += 1

print(max_l)
for e in max_list:
    print(e, end=" ")
print()