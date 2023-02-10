from collections import deque

N, M = map(int, input().split())
nums = list(map(int, input().split()))

deq = deque(i + 1 for i in range(N))
cnt = 0

for i in range(M):
    idx = deq.index(nums[i])
    deq = list(deq)
    left = len(deq[:idx])
    right = len(deq[idx:])
    deq = deque(deq)

    if left <= right:
        cnt += left
        for _ in range(left):
            deq.append(deq.popleft())
    
    else:
        cnt += right
        for _ in range(right):
            deq.appendleft(deq.pop())

    deq.popleft()

print(cnt)