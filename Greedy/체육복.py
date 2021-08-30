# https://programmers.co.kr/learn/courses/30/lessons/42862?language=python3

def solution(n, lost, reserve):
    # Remove the student in both sets because they have to wear the reserve cloth.
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)
    # if the student can give reserve to the student on the left give. Then check right.
    for i in list(set_reserve):
        if i - 1 in set_lost:
            set_lost.remove(i - 1)
        elif i + 1 in set_lost:
            set_lost.remove(i + 1)
    answer = n - len(set_lost)
    return answer

solution(5, [2, 4], [1, 3, 5])
