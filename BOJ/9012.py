import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    bracket = input().strip()
    stack = []
    for x in bracket:
        if x == '(':
            stack.append(x)
        else:
            if not stack:
                stack.append(x)
                break
            else:
                stack.pop()
                
    if stack:
        print('NO')
    else:
        print('YES')