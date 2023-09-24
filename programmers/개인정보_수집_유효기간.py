def solution(today, terms, privacies):
    answer = []
    
    dic = {}
    for term in terms:
        type, exp = term.split()
        dic[type] = int(exp)
    
    dates = []
    for privacy in privacies:
        date_str, term = privacy.split()
        y, m, d = map(int, date_str.split('.'))
        date = (y * 12 * 28) + (m * 28) + d
        date += dic[term] * 28 - 1
        dates.append(date)
    
    t_y, t_m, t_d = map(int, today.split('.'))
    t_date = (t_y * 12 * 28) + (t_m * 28) + t_d
    for i, date in enumerate(dates):
        if date < t_date:
            answer.append(i+1)    
    
    return answer


# 정해 코드

def to_days(date):
    year, month, day = map(int, date.split("."))
    return year * 28 * 12 + month * 28 + day

def solution(today, terms, privacies):
    months = {v[0]: int(v[2:]) * 28 for v in terms}
    today = to_days(today)
    expire = [
        i + 1 for i, privacy in enumerate(privacies)
        if to_days(privacy[:-2]) + months[privacy[-1]] <= today
    ]
    return expire