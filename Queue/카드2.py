# https://www.acmicpc.net/problem/2164
import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
cards = deque()

for i in range(1, n+1):
    cards.append(i)

if len(cards) == 1:
    print(cards[0])
else:
    while True:
        cards.popleft()
        cards.append(cards.popleft())
    
        if len(cards) == 1:
            print(cards[0])
            break

