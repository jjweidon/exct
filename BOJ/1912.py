"""
1. 아이디어
- 최대연속합을 저장하고 더 큰 연속합이 나오면 갱신
2. 시간복잡도
- O(N) 가능
3. 자료구조
- nums: int[n]
"""

n = int(input())
nums = list(map(int, input().split()))

maxum = -1000
tmp = 0
for num in nums:
    tmp = num if num >= tmp + num else tmp + num
    
    if maxum < tmp:
        maxum = tmp

print(maxum)