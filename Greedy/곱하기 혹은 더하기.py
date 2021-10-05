n = input() # do not read int because it does not count 0 if it starts with 0
array = []

for i in n:
    array.append(i)

array = list(map(int, array)) # convert str to int 
result = array[0] # initial calculation start with the first number

for i in range(1, len(array)): # it starts with second index because first number is already in the result
    if array[i - 1] == 0 or array[i - 1] == 1: # if the previous number is 0 or 1, adding is better
        result += array[i]
    else: # if not multiply is always better
        result *= array[i]

print(result)

# input example
# 02984

# output example
# 576
