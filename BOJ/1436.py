N = int(input())
find = 0

i = 666
while True:
    num = str(i)
    cnt6 = 1
    for j in range(1,len(num)):
        if int(num[j-1]) == int(num[j]) == 6:
            cnt6 += 1
            if cnt6 == 3:
                break
        else:
            cnt6 = 1
    if cnt6 == 3:
        find += 1
        if find == N:
            print(i)
            break
    i += 1