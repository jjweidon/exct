word = input().upper()

list_word = list(set(word))

cnt = []

for i in list_word:
    cnt.append(word.count(i))

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(list_word[cnt.index(max(cnt))])