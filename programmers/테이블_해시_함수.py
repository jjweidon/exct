def solution(data, col, row_begin, row_end):
    # 정렬
    data.sort(key=lambda x: (x[col-1], -x[0]))
    
    # S_i XOR
    answer = 0
    for i in range(row_begin-1, row_end):
        S_i = 0
        for element in data[i]:
            S_i += element % (i+1)
        answer ^= S_i
    
    return answer