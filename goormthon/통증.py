N = int(input())

rs = 0

rs += N // 14
N %= 14

rs += N // 7
N %= 7

rs += N

print(rs)


# 정해 코드

N = int(input())
result = 0

# [14, 7, 1] 이라는 배열의 각 원소 item 에 대하여
for item in [14, 7, 1]:
	result += N // item
	N %= item

print(result)