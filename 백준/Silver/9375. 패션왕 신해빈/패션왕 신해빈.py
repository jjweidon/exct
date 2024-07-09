import sys
input = sys.stdin.readline

T = int(input()) # 테스트 케이스
result = [] # 테스트 케이스마다 결과 값을 리스트로 저장
"""
1. 의상의 종류를 키값으로 종류 별 몇개의 옷이 있는지 딕셔너리로 저장
2. 총 옷의 수 + 의상 종류 별 의상 수 곱셈 으로 결과 저장 : 틀림
	-> 의상 종류 별 의상 수 + 1(그 의상을 안입은 경우) 곱셈 후 모두 안입은 경우 제외(-1)
"""
for _ in range(T):
    closet = dict() # 케이스의 의상 정보 딕셔너리
    n = int(input()) # 케이스의 총 의상 수
    for _ in range(n):
        x, cloth = map(str, input().split())
        if cloth in closet:
            # 입력받은 의상 종류가 딕셔너리에 있으면 해당 value 1 증가
            closet[cloth] += 1
        else:
            # 입력받은 의상 종류가 딕셔너리에 없으면 value = 1 로 키를 생성
            closet[cloth] = 1
        
    mul = 1
    for val in closet.values():
        mul *= val + 1 # 각 종류의 의상을 안입은 경우도 추가(+1)
    result.append(mul - 1) # 모두 안입은 경우 제외(-1)

for x in result:
    print(x)