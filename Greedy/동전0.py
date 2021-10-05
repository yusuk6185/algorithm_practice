# https://www.acmicpc.net/problem/11047

N, K = map(int, input().split()) 
value_list = [] 
for _ in range(N): 
    value = int(input()) 
    if value <= K: 
        value_list.append(value) 
cnt = 0 
for i in range(len(value_list)):
    value = value_list[(len(value_list))-i-1]
    cnt += (K // value) 
    K = K%value 

print(cnt)

# another solution
n,k=map(int,input().split());c=0 

for i in reversed(eval("int(input()),"*n)):
    c+=k//i;k=k%i 

print(c)

