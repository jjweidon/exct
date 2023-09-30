def solution(name):
    answer = 0
    lsts = []
    zeros = []
    for i, x in enumerate(name):
        num = min(ord(x) - 65, 91 - ord(x))
        lsts.append(num)
        if num == 0:
            zeros.append(i)

    cuts = []
    temp = []
    for i in range(len(zeros)):
        if not temp:
            temp.append(zeros[i])
        else:
            if zeros[i] - temp[-1] == 1:
                temp.append(zeros[i])
            else:
                cuts.append((temp[0], temp[-1]))
                temp = [zeros[i]]
    if temp:
        cuts.append((temp[0], temp[-1]))

    move = len(name) - 1
    for cut in cuts:
        minc, maxc = min(cut[0] - 1, len(lsts) - cut[1] - 1), max(cut[0] - 1, len(lsts) - cut[1] - 1)
        minc = 0 if minc < 0 else minc
        maxc = 0 if maxc < 0 else maxc
        move = min(move, minc * 2 + maxc)

    return sum(lsts) + move


# 정해 코드

def solution(name):
    answer = 0
    n = len(name)

    def alphabet_to_num(char):
        num_char = [i for i in range(14)] + [j for j in range(12, 0, -1)]
        return num_char[ord(char) - ord('A')]

    for ch in name:
        answer += alphabet_to_num(ch)

    move = n - 1
    for idx in range(n):
        next_idx = idx + 1
        while (next_idx < n) and (name[next_idx] == 'A'):
            next_idx += 1
        distance = min(idx, n - next_idx)
        move = min(move, idx + n - next_idx + distance)

    answer += move
    return answer