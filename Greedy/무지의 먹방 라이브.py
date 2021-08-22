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
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))
    
    sum_value = 0
    previous = 0
    length = len(food_times)

    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now

    result = sorted(q, key = lambda x: x[1])
    return result[(k - sum_value) % length][1]

print(solution([3,1,2],5))