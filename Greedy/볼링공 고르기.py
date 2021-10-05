# n, m = map(int, input().split())

# array = list(map(int, input().split()))

# count = 0
# for i in range(n):
#     for j in range(n):
#         if i != j and array[i] != array[j]: # count if the pair doesn't have the same weight
#             count += 1

# print(count//2) # divide by 2 because of duplicates

# example input
# 5 3
# 1 3 2 3 2

# example output
# 8

# another answer
n, m = map(int, input().split())
array = list(map(int, input().split()))

data = [0] * 11

# record the number of balls according to their weight
for i in array:
    data[i] += 1

result = 0

for i in range(1, m + 1): # for each weight
    n -= data[i]
    result += data[i] * n # get possible pairs

print(result)