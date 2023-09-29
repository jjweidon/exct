def solution(sizes):
    maxw, maxh = 0, 0
    for i, size in enumerate(sizes):
        w = max(size[0], size[1])
        h = min(size[0], size[1])
        maxw = max(maxw, w)
        maxh = max(maxh, h)

    return maxw * maxh


# 정해 코드

def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)