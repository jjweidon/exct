import sys
input = sys.stdin.readline

N = int(input())
meeting = dict()

for i in range(N):
    start, end = map(int, input().split())
    if start not in meeting: # 새로운 시작시간이 입력되면 시작시간으로 key를 생성해 딕셔너리에 저장
        meeting[start] = end 
    else:
        if end < meeting[start]: # 기존에 있던 시작시간이 입력되면 더 작은 종료시간을 value로 업데이트
            meeting[start] = end
sort_meeting = sorted(meeting.items()) # 시작시간 기준으로 오름차순 정렬 (리스트)

# 핵심은 종료시간. 가장 작은 종료시간을 찾고, 그 이후 시작시간들 기준으로 가장 작은 종료시간 찾기를 반복

cnt = 1
minEnd = sort_meeting[0][1] # 가장 작은 종료시간

for i in range(1, len(sort_meeting)): # sort_meeting 인덱스를 하나씩 탐색하며 (O(N))
    if minEnd <= sort_meeting[i][0]: # 시작시간이 가장 작은 종료시간보다 크거나 같으면
        cnt += 1 # 카운트 업!
        minEnd = sort_meeting[i][1] # 가장 작은 종료시간을 해당 인덱스의 종료시간으로 업데이트
        continue

    elif minEnd > sort_meeting[i][1]: # 그 외 가장 작은 종료시간보다 더 작은 종료시간이 등장하면
        minEnd = sort_meeting[i][1] # 가장 작은 종료시간을 해당 종료시간으로 업데이트

print(cnt) # 최종 카운트를 출력