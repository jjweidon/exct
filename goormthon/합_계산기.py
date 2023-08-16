T = int(input())
sum = 0
for _ in range(T):
    a, cal, b = input().split()
    a, b = int(a), int(b)
    if cal == '+':
        sum += a + b
    if cal == '-':
        sum += a - b
    if cal == '*':
        sum += a * b
    if cal == '/':
        sum += a // b

print(sum)