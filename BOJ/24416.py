def fib(n):
    cnt2 = 0
    f = [0] * 40
    f[0], f[1] = 1, 1
    for i in range(2, n):
        f[i] = f[i - 1] + f[i - 2]
        cnt2 += 1
    
    return f[n - 1], cnt2

n = int(input())
fibonacci = fib(n)
print(fibonacci[0], fibonacci[1])