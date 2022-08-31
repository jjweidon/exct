import sys; input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

prefix = [0]
temp = 0
for n in nums:
    temp += n
    prefix.append(temp)

result = []
for _ in range(M):
    i, j = map(int, input().split())
    result.append(prefix[j]-prefix[i-1])

print("\n".join(map(str, result)))