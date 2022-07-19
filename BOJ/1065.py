N = int(input())
cnt = 0

def hansoo(x):
    find = True
    cha = int(x[0])-int(x[1])
    for i in range(1,len(x)-1):
        if int(x[i])-int(x[i+1]) != cha:
            find = False
            break
    if find:
        global cnt
        cnt += 1
            
            
for num in range(1,N+1):
    if num < 100:
        cnt += 1
    else:
    	hansoo(str(num))
print(cnt)