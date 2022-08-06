import math
import sys
input = sys.stdin.readline

def findGCD(a, b):
    # 유클리드 호제법으로 최대공약수(gcd) 찾기
    while b > 0:
        temp = b
        b = a % b
        a = temp
    return a

# 입력
N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))
nums.sort()

# nums[i] - nums[i-1] 을 리스트(interval)에 저장
interval = []
for i in range(1,N):
    interval.append(nums[i] - nums[i-1])

# findGCD 함수를 통해 interval 리스트에 있는 수들의 최대공약수(gcd) 찾기
gcd = interval[0]
for i in range(1,N-1):
    if gcd > interval[i]:
        gcd = findGCD(gcd, interval[i])
    else:
        gcd = findGCD(interval[i], gcd)

# gcd의 약수를 모두 구해서 오름차순 출력 (Time Complexity: O(sqrt(N)))
result = set() # 집합 자료형으로 중복 제거
for i in range(int(math.sqrt(gcd))):
    i += 1
    if gcd % i == 0:
        result.add(i)
        result.add(gcd//i)
result.remove(1)
# 집합을 리스트로 형변환 후 정렬
M = list(result)
M.sort()
for x in M:
    print(x, end = ' ')