N = int(input())

def to1(n):
    if n <= 1:
        return 0
    elif n <= 3:
        return 1
    a = to1(n//2) + (n%2) + 1
    b = to1(n//3) + (n%3) + 1
    return min(a, b)

print(to1(N))