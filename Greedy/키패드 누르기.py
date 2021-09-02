# https://programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    answer = ''
    key_dict = {1:(0,0), 2:(0,1), 3:(0,2), # dictionary of key pad position
                4:(1,0), 5:(1,1), 6:(1,2),
                7:(2,0), 8:(2,1), 9:(2,2),
                '*':(3,0), 0:(3,1), '#':(3,2)}
    left = [1, 4, 7]
    right = [3, 6, 9]
    lhand = '*' # current key for left hand
    rhand = '#' # current key for right hand
    for i in numbers:
        if i in left: # if the key is for left hand only
            answer += 'L'
            lhand = i
        elif i in right: # if the key is for right hand only
            answer += 'R'
            rhand = i
        else: # if the key is in the middle
            curPos = key_dict[i] 
            lPos = key_dict[lhand]
            rPos = key_dict[rhand]
            # calculate the Manhattan Distance for left and right hands
            ldist = abs(curPos[0]-lPos[0]) + abs(curPos[1]-lPos[1])
            rdist = abs(curPos[0]-rPos[0]) + abs(curPos[1]-rPos[1])

            # select neareast hand
            if ldist < rdist: 
                answer += 'L' 
                lhand = i
            elif ldist > rdist:
                answer += 'R'
                rhand = i
            else: # if the distance is same for both hands, select familiar hand
                if hand == 'left':
                    answer += 'L'
                    lhand = i
                else:
                    answer += 'R'
                    rhand = i
    return answer
