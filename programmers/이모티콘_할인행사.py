import math

def solution(users, emoticons):
    N = len(users)
    M = len(emoticons)
    discounts = [[0] * 4 for _ in range(M)]
    
    for i, emoticon in enumerate(emoticons):
        for j, rate in enumerate([10, 20, 30, 40]):
            discounts[i][j] = emoticon * (100-rate) // 100
    
    options = []
    def dfs(i, temp):
        if i == M:
            options.append(list(temp))
            return
        for k in range(4):
            temp.append((discounts[i][k], k+1))
            dfs(i+1, temp)
            temp.pop()
    dfs(0, [])
    
    result = []
    for option in options:
        emoticon_plus = 0
        total_amount = 0
        for user in users:
            sale = math.ceil(user[0] / 10)
            price = 0
            for e in option:
                if e[1] >= sale:
                    price += e[0]
            if price >= user[1]:
                price = 0
                emoticon_plus +=1
            total_amount += price
        result.append([emoticon_plus, total_amount])
    result.sort(key=lambda x: (x[0], x[1]))

    return result[-1]