from collections import deque

N, M = map(int, input().split())
arr = deque(list(n for n in range(1, N+1)))
targets = list(map(int, input().split()))
cnt = 0

for target in targets:
    while True:
        if arr[0] == target:
            arr.popleft()
            break
        idx = arr.index(target)
        if idx <= len(arr) // 2:
            while arr[0] != target:
                arr.append(arr.popleft())
                cnt += 1
        else:
            while arr[0] != target :
                arr.appendleft(arr.pop())
                cnt += 1
        
print(cnt)