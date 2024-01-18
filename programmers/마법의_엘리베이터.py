def solution(storey):
    stone = 0
    while storey > 0:
        storey, num = divmod(storey, 10)
        if num > 5 or (num == 5 and storey % 10 >= 5):
            storey += 1
        stone += min(num, 10 - num)

    return stone