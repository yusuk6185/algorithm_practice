# https://programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):
    # step 1
    new_id = new_id.lower()

    # step 2
    allowed = ['-', '_', '.']
    answer = ''
    for i in new_id:
        if i.isalnum() or i in allowed:
            answer += i
            
    # step 3
    while '..' in answer:
        answer = answer.replace('..', '.')

    # step 4
    answer = answer[1:] if answer[0] == '.' and len(answer) > 1 else answer
    answer = answer[:-1] if answer[-1] == '.' else answer

    # step 5
    answer = 'a' if answer == '' else answer
    
    # step 6
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    
    # step 7
    while len(answer) < 3:
        answer += answer[-1]

    return answer

solution("=.=")