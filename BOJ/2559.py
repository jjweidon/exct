N, K = map(int, input().split())
temper = list(map(int, input().split()))

prefix_sum = [0]
for i in range(N):
    prefix_sum.append(prefix_sum[i] + temper[i])

maximum = -2e9
for i in range(K,N+1):
    temp_sum = prefix_sum[i] - prefix_sum[i-K]
    if maximum < temp_sum:
        maximum = temp_sum

print(maximum)