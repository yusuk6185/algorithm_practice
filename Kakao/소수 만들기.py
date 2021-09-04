from itertools import combinations

def isprime(n):
    for i in range(2, int(n ** 0.5) +1):
        if n % i == 0:
            return False
    return True
    

def solution(nums):
    answer = 0
    nums_comb = list(combinations(nums, 3))
    
    for i in nums_comb:
        if isprime(sum(i)):
            answer += 1

    print(answer)

solution([3, 4, 5, 6])