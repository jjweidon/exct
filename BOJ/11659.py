import sys; input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
result = []
for _ in range(M):
    i, j = map(int, input().split())
    result.append(sum(nums[i-1:j]))

print("\n".join(map(str, result)))