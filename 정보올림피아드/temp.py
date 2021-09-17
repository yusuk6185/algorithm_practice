
n = int(input())

max_l = 0
max_list = []

for i in range(n+1):
    result = [n, i]
    j = 0
    while True:
        new_num = result[j] - result[j+1]
        if new_num <= -1:
            break
        result.append(new_num)
        if max_l < len(result):
            max_l = len(result)
            max_list = result
        j += 1

print(max_l)
for i in max_list:
    print(i, end = ' ')