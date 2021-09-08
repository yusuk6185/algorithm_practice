# https://programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    d.sort()
    answer = []
    for i in range(len(d)):
        answer.append(d[i])
        if sum(answer) > budget:
            answer.pop()
            break
        elif sum(answer) == budget:
            break
    
    return len(answer)

print(solution([1,3,5,2,4], 9))

# another solution

def solution(d, budget):
    d.sort()

    while budget < sum(d):
        d.pop()
    
    return len(d)
