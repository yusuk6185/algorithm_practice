# https://www.acmicpc.net/problem/10816



def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return target
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input())
array = list(map(int, input().split()))
m = int(input()) 
target = list(map(int, input().split()))

array.sort()
dic = {}

for i in array:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

for i in range(m):
    result = binary_search(array, target[i], 0, n-1)
    if result == None:
        print(0, end = ' ')
    else:
        print(dic[target[i]], end= ' ')