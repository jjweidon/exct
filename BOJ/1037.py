N = int(input())
divisor = list(map(int, input().split()))
divisor.sort()
#가장 작은 약수와 가장 큰 약수의 곱
print(divisor[0]*divisor[-1])