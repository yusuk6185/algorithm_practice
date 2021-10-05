# https://programmers.co.kr/learn/courses/30/lessons/81301

word_list = [(0, 'zero'), (1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'), (6, 'six'), (7, 'seven'), (8, 'eight'), (9, 'nine')]

def solution(s):
    for i in word_list:
        if i[1] in s:
            s = s.replace(i[1], str(i[0]))
    return int(s)

solution("one4seveneight")