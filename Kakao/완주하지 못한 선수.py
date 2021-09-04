# https://programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    p_set = set(participant)
    c_set = set(completion)
    result = list(p_set - c_set)
    if result != []:
        return result[0]
    else:
        for i in range(len(completion)):
            p_count = participant.count(i)
            c_count = completion.count(i)
            if p_count != c_count:
                return i
    
    return None
solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])