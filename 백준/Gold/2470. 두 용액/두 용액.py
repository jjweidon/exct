N = int(input())
liquids = list(map(int, input().split()))
liquids.sort()

left, right = 0, N-1
minn = abs(liquids[left] + liquids[right])
rs = [liquids[left], liquids[right]]

while left < right:
    summ = liquids[left] + liquids[right]
    if minn > abs(summ):
        rs = [liquids[left], liquids[right]]
        minn = abs(summ)
    if summ == 0:
        break
    elif summ < 0:
        left += 1
    elif summ > 0:
        right -= 1

print(*rs)