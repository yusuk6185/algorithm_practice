# https://programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    count = 0
    zeros = 0
    for i in lottos:
        if i in win_nums:
            count += 1
        elif i == 0:
            zeros += 1

    best = count + zeros
    worst = count
    
    cases = []
    cases.append(best)
    cases.append(worst)
    
    answer = [] 
    for i in cases:
        if i == 6:
            answer.append(1)
        elif i == 5:
            answer.append(2)
        elif i == 4:
            answer.append(3)
        elif i == 3:
            answer.append(4)
        elif i == 2:
            answer.append(5)
        else:
            answer.append(6)

    return answer

# better solution

def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]

    cnt_zero = lottos.count(0) # count the number of zeros
    result = 0 
    for i in lottos:
        if i in win_nums:
            result += 1

    return rank[cnt_zero + result], rank[result]

solution([44, 1, 0, 0, 31, 25],	[31, 10, 45, 1, 6, 19])