# PyPy3으로 제출: 틀림
from itertools import permutations

N = int(input())
A = list(map(int, input().split()))
C = list(map(int, input().split()))
cal = []
for i in range(4):
    for _ in range(C[i]):
        cal.append(i)
permute = list(permutations(cal))

result = []
for express in permute:
    num = A[0]
    for i in range(1, N):
        if express[i-1] == 0:
            num += A[i]
        elif express[i-1] == 1:
            num -= A[i]
        elif express[i-1] == 2:
            num *= A[i]
        elif express[i-1] == 3:
            num //= A[i]
    result.append(num)

print(max(result))
print(min(result))