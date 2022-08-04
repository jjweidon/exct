import sys
input = sys.stdin.readline

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0: #두 입력이 모두 0이면 반복 종료
        break
    
    elif b % a == 0: #1. 첫 번째 숫자가 두 번째 숫자의 약수이다.
        print("factor")
    
    elif a % b == 0: #2. 첫 번째 숫자가 두 번째 숫자의 배수이다.
        print("multiple")
    
    else: #3. 첫 번째 숫자가 두 번째 숫자의 약수와 배수 모두 아니다.
        print("neither")