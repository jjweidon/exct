import sys
input = sys.stdin.readline

N = int(input())
num_list = map(int, input().split())
v = int(input())
count = 0

for num in num_list:
    if num == v:
        count += 1

print(count)