# 나의 풀이

user_input = input()

W, R = user_input.split()
RM = int(W) * (1+int(R)/30)
print(int(RM))


# 정해 코드

import math
W, R = map(int, input().split())
print(math.trunc(W * (1 + R / 30)))