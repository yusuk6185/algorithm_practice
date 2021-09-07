# https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    # 배열의 각 항목 / 전체 플레이어 수 
    # 항목만큼 전체 플레이어 수 감소
    result = {}
    player_num = len(stages)
    for stage in range(1, N+1):
        if player_num:
            count = stages.count(stage)
            result[stage] = count / player_num
            player_num -= count
        else:
            result[stage] = 0
    
    # value 값을 기준으로 정렬한 key 리스트를 내림차순으로 반환
    print(sorted(result, key=lambda x : result[x], reverse=True))
    
solution(5,	[2, 1, 2, 6, 2, 4, 3, 3])