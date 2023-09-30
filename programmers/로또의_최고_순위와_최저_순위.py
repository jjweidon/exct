def solution(lottos, win_nums):
    low, high = 0, 0
    for lotto in lottos:
        if lotto == 0:
            high += 1
        elif lotto in win_nums:
            low += 1
    
    high += low
    
    high = 6 if high == 0 else 7 - high
    low = 6 if low == 0 else 7 - low
    
    return high, low


# 정해 코드

def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]