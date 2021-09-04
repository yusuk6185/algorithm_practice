def solution(answers):
    num_1 = []
    num_2 = []
    num_3 = []

    # number 1
    for i in range(len(answers)):
        num_1.append((i%5)+1)

    # number 2
    array = [2,1,2,3,2,4,2,5]
    num_2 += array * (len(answers) // len(array))
    num_2 += array[:len(answers) % len(array)]

    # number 3
    array = [3,3,1,1,2,2,4,4,5,5]    
    num_3 += array * (len(answers) // len(array))
    num_3 += array[:len(answers) % len(array)]

    # count number of the correct answers for each student
    count_1 = 0
    count_2 = 0
    count_3 = 0
    for i in range(len(answers)):
        if num_1[i] == answers[i]:
            count_1 += 1
        if num_2[i] == answers[i]:
            count_2 += 1
        if num_3[i] == answers[i]:
            count_3 += 1

    # append to list if the student has the max number among the students
    answer = []
    result = [count_1, count_2, count_3]
    for i in range(len(result)):
        if result[i] == max(result):
            answer.append(i+1)
    
    return answer

# better solution

def solution(answers):
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2 ,4 ,2 ,5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx + 1)

    return result
    
solution([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])