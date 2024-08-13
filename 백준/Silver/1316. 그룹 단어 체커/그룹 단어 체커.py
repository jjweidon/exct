N = int(input())
group = 0

for _ in range(N):
    word = input()
    find_group = True
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            pass
        elif word[i] in word[i+2:]:
            find_group = False
            break
    if find_group:
        group += 1

print(group)