a, b, v = map(int, input().split())

pre_move = (v-a)//(a-b)
remainder = (v-a)%(a-b)

if remainder == 0:
    print(pre_move+1)
else:
    print(pre_move+2)