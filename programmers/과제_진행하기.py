def solution(plans):
    answer = []

    for i in range(len(plans)):
        h, m = map(int, plans[i][1].split(":"))
        plans[i][1] = h * 60 + m
        plans[i][2] = int(plans[i][2])
    plans.sort(key = lambda x: -x[1])

    todo = plans
    doing = []
    cur_time = todo[-1][1]

    while todo:
        doing.append(todo.pop())

        if todo:
            next_time = todo[-1][1]
            while doing:
                cur = doing.pop()
                if cur_time + cur[2] > next_time:
                    gap = next_time - cur_time
                    cur[2] -= gap
                    doing.append(cur)
                    break
                else:
                    cur_time += cur[2]
                    answer.append(cur[0])
            cur_time = next_time

        # 마지막 원소
        else:
            while doing:
                answer.append(doing.pop()[0])

    return answer

plans = [["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]
print(solution(plans))


# 정해 코드

def solution(plans):
    plans = sorted(map(lambda x: [x[0], int(x[1][:2]) * 60 + int(x[1][3:]), int(x[2])], plans), key=lambda x: -x[1])

    lst = []
    while plans:
        x = plans.pop()
        for i, v in enumerate(lst):
            if v[0] > x[1]:
                lst[i][0] += x[2]
        lst.append([x[1] + x[2], x[0]])
    lst.sort()

    return list(map(lambda x: x[1], lst))