def solution(s, skip, index):
    answer = []
    
    # skip을 숫자로 변환하여 리스트로 저장
    skip_lst = []
    for sk in skip:
        skip_lst.append(ord(sk) - 97) # a의 ascii코드는 97
    
    for ele in s:
        cnt = index
        current = ord(ele) - 97
        # cnt가 0이 될때까지 반복
        while cnt:
            current = (current + 1) % 26 # 나머지로 알파벳 범위를 넘어가면 0부터 시작
            if current in skip_lst: # skip_lst 안에 있는 값이면 continue
                continue
            cnt -= 1 # if문에 걸리지 않았으면 cnt - 1
        answer.append(chr(current + 97)) # 숫자에 97을 더해 문자로 변환
        
    return "".join(answer) # 리스트 -> 문자열


# 정해 코드

from string import ascii_lowercase

def solution(s, skip, index):
    result = ''

    a_to_z = set(ascii_lowercase)
    a_to_z -= set(skip)
    a_to_z = sorted(a_to_z)
    l = len(a_to_z)

    dic_alpha = {alpha:idx for idx, alpha in enumerate(a_to_z)}

    for i in s:
        result += a_to_z[(dic_alpha[i] + index) % l]

    return result