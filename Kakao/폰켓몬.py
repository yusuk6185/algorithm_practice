# https://programmers.co.kr/learn/courses/30/lessons/1845
from itertools import combinations

def solution(nums):
    N = len(nums) // 2
    ponketmon = list(set(nums))
    answer = 0
    if len(ponketmon) > N: # 최대 포켓몬 개수보다 가질 수 있는 폰켓몬 개수가 더 많으면 최대 개수 출력
        answer = N
    else: # 가능한 폰켓몬 개수가 최대 가질 수 있는 폰켓몬 개수보다 적으면 가능한 개수 출력 
        answer = len(ponketmon)
    return answer

solution([3,3,3,2,2,2])

