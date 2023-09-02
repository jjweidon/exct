N = int(input())
k = int(input())

def binarySearch(N, k):
    start = 1
    end = min(1e9, N*N)
    answer = 0

    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for i in range(1, N+1):
            cnt += min(mid // i, N)
        print(f'start: {start}, end: {end}, mid: {mid}, cnt: {cnt}')

        if cnt >= k:
            answer = mid
            end = mid - 1
        elif cnt > k:
            start = mid + 1
    return answer

print(binarySearch(N, k))


"""
1 2 3 4
2 4 6 8
3 6 9 12
4 8 12 16

1 2 2 3 3 4 4 4 6 6 8 8 9 12 12 16


"""