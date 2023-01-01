"""
1. 
- 병합정렬
2. 
- 500000log500000 = 250만 * log5
3. 
- N, K
- A[N]
- def merge(A)
- 저장 순서 rs[]
"""

N, K = map(int, input().split())
A = list(map(int, input().split()))
rs = []

def merge(marr):
    if len(marr) == 1:
        return marr

    mid = (len(marr) + 1) // 2
    left = merge(marr[:mid])
    right = merge(marr[mid:])

    i = 0
    j = 0
    tmp = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            tmp.append(left[i])
            rs.append(left[i])
            i += 1
        else:
            tmp.append(right[j])
            rs.append(right[j])
            j += 1
    
    while i < len(left):
        tmp.append(left[i])
        rs.append(left[i])
        i += 1
    while j < len(right):
        tmp.append(right[j])
        rs.append(right[j])
        j += 1
    
    return tmp

merge(A)
if len(rs) >= K:
    print(rs[K-1])
else:
    print(-1)