A, B = map(int, input().split())
C = int(input())

if B+C < 60:
    print(A, B+C)
else:
    print((A+(B+C)//60)%24, (B+C)%60)