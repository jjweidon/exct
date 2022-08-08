# 문제에서 의도한 백트랙킹을 사용하는 방법
N ,M = map(int, input().split())
s = []
check = [False] * (N+1)

def DFS():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    
    for i in range(1, N+1):
        if check[i] == True:
            continue
        s.append(i)
        check[i] = True
        DFS()
        s.pop()
        check[i] = False
DFS()

## 파이썬에 있는 itertools의 permutations를 사용하는 방법
# import itertools

# N, M = map(int, input().split())
# nums = [i for i in range(1, N+1)]
# array = itertools.permutations(nums, M)

# for x in array:
#     print(' '.join(map(str, x)))