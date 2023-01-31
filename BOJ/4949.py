import sys
input = sys.stdin.readline

while 1:
    sentence = input().rstrip()
    if sentence == '.':
        break

    stack = []
    for x in sentence:
        if x == '(':
            stack.append(x)
        elif x == '[':
            stack.append(x)
        elif x == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                print('no')
                break
        elif x == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                print('no')
                break
    else:
        if stack: print('no')
        else: print('yes')