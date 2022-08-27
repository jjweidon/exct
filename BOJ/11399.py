N = int(input())
atm = list(map(int, input().split()))
atm.sort()

time = list()
hap = 0
for x in atm:
    hap += x
    time.append(hap)
print(sum(time))