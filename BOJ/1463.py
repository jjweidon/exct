"""
1. 아이디어
- 2로 나눈것과 3으로 나눈것 중 작은 걸 택하는 재귀함수
2. 시간복잡도
O(logN) 가능
3. 자료구조
cnt: int
"""

N = int(input())

def to1(n):
    if n <= 1:
        return 0
    elif n <= 3:
        return 1
    a = to1(n//2) + (n%2) + 1
    b = to1(n//3) + (n%3) + 1
    return min(a, b)

print(to1(N))