import sys
import heapq

input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]

max_heap = []
min_heap = []

print(nums[0])
if N == 1:
    max_heap.append(-nums[0])
elif N > 1 and nums[0] > nums[1]:
    max_heap.append(-nums[1])
    min_heap.append(nums[0])
    print(-max_heap[0])
else:
    max_heap.append(-nums[0])
    min_heap.append(nums[1])
    print(-max_heap[0])

len_max_heap = len(max_heap)
len_min_heap = len(min_heap)

for i in range(2, N):
    num = nums[i]
    left = -max_heap[0]
    right = min_heap[0]
    
    if len_max_heap == len_min_heap:
        if num > right:
            right = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -right)
            heapq.heappush(min_heap, num)
        else:
            heapq.heappush(max_heap, -num)
        len_max_heap += 1

    else:
        if num < left:
            left = -heapq.heappop(max_heap)
            heapq.heappush(max_heap, -num)
            heapq.heappush(min_heap, left)
        else:
            heapq.heappush(min_heap, num)
        len_min_heap += 1
    print(-max_heap[0])