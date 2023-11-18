def solution(book_time):
    # 분 단위로 통일
    decimal_time = []
    for bt in book_time:
        temp = []
        for k in range(2):
            h, m = map(int, bt[k].split(":"))
            temp.append(h * 60 + m)
        decimal_time.append(temp)
    decimal_time.sort(key=lambda x : x[0])
    
    rooms = [decimal_time[0][1]]
    for i in range(1, len(decimal_time)):
        start = decimal_time[i][0]
        end = decimal_time[i][1]
        
        for j, room in enumerate(rooms):
            if room + 10 <= start:
                rooms[j] = end
                break
        else:
            rooms.append(end)
    
    return len(rooms)