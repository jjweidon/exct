N = int(input())
numsN = list(map(int, input().split()))
numsN.sort()
M = int(input())
numsM = list(map(int, input().split()))

def search(arr, target):
    start = 0
    end = len(numsN)-1

    while start <= end:
        mid = (start + end) // 2
        if numsN[mid] == target:
            return 1
        elif numsN[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0

for num in numsM:
    print(search(numsN, num))