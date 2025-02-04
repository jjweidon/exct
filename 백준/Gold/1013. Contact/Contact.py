import re

T = int(input())
rule = re.compile("(100+1+|01)+")
for _ in range(T):
    wave = input().rstrip()
    if rule.fullmatch(wave):
        print("YES")
    else:
        print("NO")