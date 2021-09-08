# https://programmers.co.kr/learn/courses/30/lessons/77884


def solution(left, right):
    answer = 0
    # 설정된 구간의 모든 수 중에
    for num in range(left, right + 1):
        measures = []
        # 1 부터 num 까지의 모든 수를 나누어서 나뉘어 떨어진다면 약수로 추가
        for measure in range(1, num + 1):
            if num % measure == 0:
                measures.append(measure)
        # 각 num 의 약수의 총 개수가 짝수라면 answer 에서 더하고 아니면 뺀다.
        if len(measures) % 2 == 0:
            answer += num
        else:
            answer -= num

    return answer 

solution(13, 17)