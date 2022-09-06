N, M = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()

def binary(M, trees):
    start = 1
    end = trees[-1]
    while start <= end:
        cuts = 0
        mid = (start + end) // 2
        for tree in trees:
            if mid < tree:
                cuts += tree - mid
        if cuts == M:
            return mid
        elif cuts < M:
            end = mid - 1
        else:
            start = mid + 1
    return end

print(binary(M, trees))