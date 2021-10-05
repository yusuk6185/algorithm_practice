def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i + 1

print("Enter the number of elements you want to create and the string you want to find after a space.")
input_data = input().split()

n = int(input_data[0])
target = input_data[1]

print("Enter the strings with the number of elements selected identified with a space.")
array = input().split()

print(sequential_search(n, target, array))