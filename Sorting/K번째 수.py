# https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    new_arr = []
    answer = []
    for i in range(len(commands)):
        new_arr.append(array[commands[i][0]-1:commands[i][1]])
        new_arr[i].sort()
        answer.append(new_arr[i][commands[i][2]-1])
    
    return answer

# better answer
def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        answer.append(sorted(array[i - 1: j])[k - 1])
    return answer

solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])
