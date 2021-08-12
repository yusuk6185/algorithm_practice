# Time complexity: O(N + K)

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# declare a list that contains all of the range
count = [0] * (max(array) + 1)

for i in range(len(array)):
    # add count of the coresponding data
    count[array[i]] += 1

# check sort information recorded in the list
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end = ' ')