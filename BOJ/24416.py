def fib(n, cnt): 
    if n == 1 or n == 2:
        cnt += 1
        return 1, cnt
    else:
        return (fib(n - 1, cnt)[0] + fib(n - 2, cnt)[0], cnt)

def fibonacci(n):
    cnt2 = 0
    f = [0, 1, 1]
    for i in range(3, n + 1):
        f.append(f[i - 1] + f[i - 2])
        cnt2 += 1
    return cnt2

n = int(input())
cnt1 = 0

print(fib(n, cnt1)[0], fibonacci(n))