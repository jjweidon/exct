def solution(gems):
    target = len(set(gems))
    s, e = 0, 0
    dic = {}
    rs, re = 0, len(gems)-1
    
    while e < len(gems):
        dic[gems[e]] = dic.get(gems[e], 0) + 1
        
        while len(dic) == target:
            if re - rs > e - s:
                rs, re = s, e
            dic[gems[s]] -= 1
            if dic[gems[s]] <= 0:
                del dic[gems[s]]
            s += 1
        e += 1
        
    return rs+1, re+1
    