def solution(numbers, target):
    rs = [[] for _ in range(len(numbers))]
    rs[0].append(numbers[0])
    rs[0].append(-numbers[0])
    for i in range(1, len(numbers)):
        for r in rs[i-1]:
            rs[i].append(r + numbers[i])
            rs[i].append(r - numbers[i])

    return rs[len(numbers)-1].count(target)


# 12분37초
# 정해 코드

def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])