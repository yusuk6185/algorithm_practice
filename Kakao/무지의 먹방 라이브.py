#     data = food_times
#     count = 0

#     for i in range(k + 1):
#         n = i % len(data)
#         if data[n] == 0:
#             count += 1
#             continue
#         data[n] -= 1
#         count += 1
#         print(data)
#         print(count)
    
#     if data == [0 for i in range(len(data))]:
#         print(-1)

# print(solution([3, 1, 2], 5))

import heapq

def solution(food_times, k):
    # if ate all the foods before the connection loss print -1
    if sum(food_times) <= k:
        return -1

    q = []
    # insert all the foods in to the queue
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1)) # prioritized by the food time and labelled with food number
    
    # time taken to eat
    sum_value = 0
    # time taken to finish previous food
    previous = 0
    # number of food left
    length = len(food_times)

    # compare k with sum_value + (current food time - previous food time) * current number of food 
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1 # subtract the food finished
        previous = now # reset the previous food time

    # print the food number among the food left
    result = sorted(q, key = lambda x: x[1]) # sort the food by the food number
    return result[(k - sum_value) % length][1]

print(solution([3,1,2],5))