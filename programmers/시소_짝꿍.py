def solution(weights):
    answer = 0
    
    count = [0 for _ in range(1001)]
    for w in weights:
        count[w] += 1
    
    for weight in weights:
        temp = set()
        for n in range(2, 5):
            k = weight * n
            for m in range(2, 5):
                if n == m:
                    continue
                if k % m == 0 and 100 <= k // m <= 1000:
                    temp.add(k // m)
        
        for pair in temp:
            answer += count[pair]
        if count[weight] >= 2:
            answer += count[weight]-1

    return answer // 2