s = input()

count0 = 0 # counter to make all 0
count1 = 0 # counter to make all 1

if s[0] == '0': # count first digit
    count1 += 1
else:
    count0 += 0

for i in range(len(s) - 1): 
    if s[i] != s[i+1]: # if the next digit is different increment the counter
        if s[i+1] == '0':
            count1 += 1
        else:
            count0 += 1

print(min(count0, count1))

# example input
# 0001100

# example output
# 1