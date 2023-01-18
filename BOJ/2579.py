"""
1. 아이디어
- 마지막 인덱스부터 시작해서 연속 한개일 때: 둘 중 더 큰수로 뛰기 / 연속 두개일 때: 두칸 뛰기
2. 시간복잡도
- O(N/2)
3. 자료구조
- stair: int[] / step: bool
"""

import sys
input = sys.stdin.readline

N = int(input())
stair = [0] * N
for i in range(N):
    stair[i] = int(input())

step = False
index = N - 1
rs = stair[index]
while index >= 2:
    if step:
        index -= 2
        step = False
        
    else:
        if stair[index-1] >= stair[index-2]:
            index -= 1
            step = True
        else:
            index -= 2
            # step = False
    
    rs += stair[index]

# index error를 회피하기 위해 index = 2까지 while 돌리고 그 이하는 따로 처리
if index and not step:
    rs += stair[0]

print(rs)