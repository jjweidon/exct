def solution(keymap, targets):
    alpha = [0 for _ in range(28)]
    for j in range(len(keymap)):
        for i in range(len(keymap[j])):
            idx = ord(keymap[j][i]) - 65
            alpha[idx] = min(alpha[idx], i+1) if alpha[idx] else i+1
    
    answer = []
    for target in targets:
        temp = 0
        for x in target:
            idx = ord(x) - 65
            if not alpha[idx]:
                answer.append(-1)
                break
            else:
                temp += alpha[idx]
        else:
            answer.append(temp)
    
    return answer


# 정해 코드

def solution(keymap, targets):
    answer = []
    hs = {}
    for k in keymap:
        for i, ch in enumerate(k):
            hs[ch] = min(i + 1, hs[ch]) if ch in hs else i + 1

    for i, t in enumerate(targets):
        ret = 0
        for ch in t:
            if ch not in hs:
                ret = - 1
                break
            ret += hs[ch]
        answer.append(ret)

    return answer