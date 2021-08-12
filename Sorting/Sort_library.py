array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# sort with two list variables
result = sorted(array)
print(result)

# sort with one list variable
array.sort()
print(array)

# sort with key
array = [('banana', 2), ('apple', 5), ('carrot', 3)]

def setting(data):
    return data[1]

result = sorted(array, key = setting)
print(result)
# print(setting(array))