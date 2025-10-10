def solution(numbers, hand):
    answer = ''
    
    keypad = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"],
        ["*", "0", "#"]
    ]
    cl = [3, 0]
    cr = [3, 2]
    
    def find_index(number):
        for y in range(4):
            for x in range(3):
                if str(number) == keypad[y][x]:
                    return [y, x]
    
    def get_distance(idx1, idx2):
        y1, x1 = idx1
        y2, x2 = idx2
        return abs(y1 - y2) + abs(x1 - x2)
    
    for number in numbers:
        if number in (1, 4, 7):
            answer += "L"
            cl = find_index(number)
        elif number in (3, 6, 9):
            answer += "R"
            cr = find_index(number)
        else:
            idx = find_index(number)
            dl = get_distance(cl, idx)
            dr = get_distance(cr, idx)
            if dl < dr or (dl == dr and hand == "left"):
                answer += "L"
                cl = idx
            elif dr < dl or (dl == dr and hand == "right"):
                answer += "R"
                cr = idx
    
    return answer