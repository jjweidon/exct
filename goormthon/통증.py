N = int(input())

rs = 0

rs += N // 14
N %= 14

rs += N // 7
N %= 7

rs += N

print(rs)