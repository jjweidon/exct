import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
check = list(map(int, input().split()))
answer = []

dic = Counter(cards)
for x in check:
    answer.append(dic[x])

for x in answer:
    print(x, end=' ')