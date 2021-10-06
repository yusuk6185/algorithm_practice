# https://programmers.co.kr/learn/courses/30/lessons/42578?language=python3

def solution(clothes):
    closet = {}
    for cloth in clothes:
        key = cloth[1]
        value = cloth[0]
        if key in closet:
            closet[key].append(value)
        else:
            closet[key] = [value]
    
    result = 1
    for key in closet.keys():
        result *= len(closet[key]) + 1
    return result - 1