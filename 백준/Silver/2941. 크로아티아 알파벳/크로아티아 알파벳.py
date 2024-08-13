word = input()
i = len(word) - 1
cnt = 0

while i >= 0:
    if word[i] == '=':
        if i >= 1 and word[i-1] in ('c', 's'):
            i -= 2
        elif i >= 1 and word[i-1] == 'z':
            if i >= 2 and word[i-2] == 'd':
                i -= 3
            else:
                i -= 2
        else:
            i -= 1

    elif word[i] == '-':
        if i >= 1 and word[i-1] in ('c', 'd'):
            i -= 2
        else:
            i -= 1

    elif word[i] == 'j':
        if i >= 1 and word[i-1] in ('l', 'n'):
            i -= 2
        else:
            i -= 1

    else:
        i -= 1
    
    cnt += 1

print(cnt)