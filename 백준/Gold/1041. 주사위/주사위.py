N = int(input())
dice = list(map(int, input().split()))
A = min(dice[0], dice[-1])
B = min(dice[1], dice[-2])
C = min(dice[2], dice[-3])
three = A + B + C
two = min(A + B, B + C, A + C)
one = min(A, B, C)

if N == 1:
    print(sum(sorted(dice)[:5]))
else:
    print(
        three * 4 +
        two * (4 * (2 * N - 3)) +
        one * ((N - 2) * (5 * N - 6))
    )