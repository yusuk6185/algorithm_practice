# https://programmers.co.kr/learn/courses/30/lessons/76501

def solution(absolutes, signs):
    for i in range(len(absolutes)):
        if signs[i] == False:
            absolutes[i] = -absolutes[i]
    answer = sum(absolutes)
    return answer

solution([4,7,12], [True,False,True])