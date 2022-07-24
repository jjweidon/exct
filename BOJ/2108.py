from collections import Counter
import sys

N = int(sys.stdin.readline())
nums = []
for _ in range(N):
    nums.append(int(sys.stdin.readline()))

#산술평균
print(round(sum(nums)/len(nums)))

#중앙값
nums.sort()
print(nums[round(len(nums)/2)])
      
#최빈값
if N == 1:
    print(nums[0])
else:
    li = Counter(nums).most_common(2)
    if li[0][1] > li[1][1]:
        print(li[0][0])
    else:
        print(li[1][0])

#범위
print(nums[-1]-nums[0])