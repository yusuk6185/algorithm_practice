# https://programmers.co.kr/learn/courses/30/lessons/68935

def solution(n):
    answer = ''
    result = 0
    # n을 3으로 나눌 때마다 3의 지수가 하나씩 낮아짐. 3진수로 볼 땐 자리가 바뀜.
    # ex) 27 == 3**3 -> 27 // 3 = 9 == 3**2, 9 // 3 = 3 == 3**1, 3 // 3 = 1 == 3**0
    while n >= 1:
       rest = n % 3 # 나머지가 3진법으로 표현됨
       n //= 3
       answer += str(rest) # str로 추가하여 값이 더해지지 않음
    print(answer)
    for index, digit in enumerate(range(len(answer) - 1, -1, -1)): 
        result += int(answer[digit]) * 3**index # 3진법을 10진법으로 바꿈

    return result

# another solution

def solution(n):
    answer = []
    while True: # break 하기 전까지 반복
        n, rest = divmod(n, 3)
        answer.append(rest)

        if n == 0:
            break

    return sum([i * 3**idx for idx, i in enumerate(reversed(answer))])

solution(125)
