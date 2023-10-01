def solution(cards):
    answer = 0
    n = len(cards)
        
    for i in range(n):
        score = 0
        visited = [False for _ in range(n)]
        
        def cnt(idx):
            rs = 0
            cur = idx
            while not visited[cur]:
                visited[cur] = True
                rs += 1
                cur = cards[cur] - 1
            return rs
                
        group1 = cnt(i)
        for j in range(n):
            if not visited[j]:
                group2 = cnt(j)
                if not group2:
                    score = 0
                else:
                    score = group1 * group2
                answer = max(answer, score)
    
    return answer

# 정해 코드

def solution(cards):
    answer = []
    for i in range(len(cards)):
        tmp = []
        while cards[i] not in tmp:
            tmp.append(cards[i])
            i = cards[i] - 1
        answer.append([] if sorted(tmp) in answer else sorted(tmp))
    answer.sort(key=len)

    return len(answer[-1]) * len(answer[-2])