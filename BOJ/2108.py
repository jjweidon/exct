N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))

#산술평균
print(round(sum(nums)/len(nums)))

#중앙값
nums.sort()
print(nums[round(len(nums)/2)])
      
#최빈값
if len(nums) == 1:
    print(nums[0])
else:
    mode = list(set(nums))
    mode.sort()
    cnt = []

    count = 1
    for i in range(1,len(nums)):
        if nums[i] == nums[i-1]:
            count += 1
        else:
            cnt.append(count)
            count = 1
    cnt.append(count)
    if cnt.count(max(cnt)) < 2:
        print(mode[cnt.index(max(cnt))])
    else:
        find = False
        for j in range(0,len(cnt)):
            if (cnt[j] == max(cnt)) ^ find:
                find = True
            elif (cnt[j] == max(cnt)) & find:
                print(mode[j])
                break

#범위
print(nums[-1]-nums[0])