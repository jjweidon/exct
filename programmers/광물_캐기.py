def solution(picks, minerals):
    lst = []
    for i in range(len(minerals) // 5 + 1):
        s = i * 5
        e = min((i+1) * 5, len(minerals))
        mines = minerals[s:e]
        pirodo = [0, 0, 0]
        for mine in mines:
            if mine == 'diamond':
                pirodo[0] += 1
                pirodo[1] += 5
                pirodo[2] += 25
            elif mine == 'iron':
                pirodo[0] += 1
                pirodo[1] += 1
                pirodo[2] += 5
            elif mine == 'stone':
                pirodo[0] += 1
                pirodo[1] += 1
                pirodo[2] += 1
        lst.append(pirodo)
    
    lst = lst[:sum(picks)]
    lst.sort(key = lambda x: x[2])

    answer = 0
    for i in range(3):
        for _ in range(picks[i]):
            if not lst:
                break
            m = lst.pop()
            answer += m[i]
    
    return answer


# 정해 코드

def solution(picks, minerals):
    def solve(picks, minerals, fatigue):
        if sum(picks) == 0 or len(minerals) == 0:
            return fatigue
        result = [float('inf')]
        for i, fatigues in enumerate(({"diamond": 1, "iron": 1, "stone": 1},
                                    {"diamond": 5, "iron": 1, "stone": 1},
                                    {"diamond": 25, "iron": 5, "stone": 1},)):
            if picks[i] > 0:
                temp_picks = picks.copy()
                temp_picks[i] -= 1
                result.append(
                    solve(temp_picks, minerals[5:], fatigue + sum(fatigues[mineral] for mineral in minerals[:5])))
        return min(result)

    return solve(picks, minerals, 0)