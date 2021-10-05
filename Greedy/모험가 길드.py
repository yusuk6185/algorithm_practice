n = int(input())

array = list(map(int,input().split()))
array.sort()

result = 0 # total number of group
count = 0 # current group

for i in array:
    count += 1 # add member to the group
    if count >= i: # if the number of current group member is bigger than current fear
        result += 1 # increment total number of groups
        count = 0 # reset the current group

print(result)

# input example
# 5

# output example
# 2 3 1 2 2