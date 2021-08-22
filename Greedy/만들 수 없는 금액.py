# This code can get the answer but it takes too long.
# Use the second code below.

# n = int(input())
# array = []

# array = list(map(int, input().split()))
# array.sort(reverse=True) # sort the array so the bigger number comes first

# natural = list(range(1, 1000000)) # array of natural numbers

# count = 0 
# can_make = []

# for i in natural: 
#     count = i
#     for j in array:
#         if j <= count: # subtract the natural number with the biggest number in the list yet smaller than the natural number
#             count -= j
#         if count == 0: # when it reaches 0, add the number to can_make list
#             can_make.append(i)
#             break
                
# for i in natural:
#     if i not in can_make: # compare the can_make list with the natural number list and print the smallest number
#         print(i)
#         break

# example input
# 5
# 3 2 1 1 9

# example output
# 8

# Answer

n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data: # the number smaller than the target can be made
    if target < x: # break if the target cannot be made
        break
    target += x
    print(target)
