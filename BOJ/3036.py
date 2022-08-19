N = int(input())
ring = list(map(int, input().split()))

def findGCD(a, b):
    while b > 0:
        temp = b
        b = a % b
        a = temp
    return a

gcd = 0
for i in range(1, N):
    gcd = findGCD(max(ring[0], ring[i]), min(ring[0], ring[i]))
    print('{}/{}'.format(ring[0]//gcd, ring[i]//gcd))