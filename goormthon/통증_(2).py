N = int(input())
A, B = map(int, input().split())

for i in range(N // B, -1, -1):
    rs = i
    temp = N - (B * i)
    if temp % A == 0:
        rs += temp // A
        print(rs)
        break
    
else:
    print(-1)