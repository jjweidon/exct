import sys
input = sys.stdin.readline

X = int(input())
N = int(input())
script = 0 # 영수증 가격 합계

for i in range(N):
    a, b = map(int, input().split()) # a : 물건의 가격, b : 물건의 개수
    script += a * b 

if X == script:
    print("Yes")
else:
    print("No")