N = int(input())
S = input()
P = set()

for i in range(1, N-1):
    P.add(S[:i])
    for j in range(i,N-1):
        P.add(S[i:j+1])
        P.add(S[j+1:])
lst = list(P)
lst.sort()

dct = {}
for i in range(len(lst)):
    dct[lst[i]] = i+1

maxx = 0
for i in range(1, N-1):
    for j in range(i,N-1):
        score = dct[S[:i]] + dct[S[i:j+1]] + dct[S[j+1:]]
        if score > maxx:
            maxx = score

print(maxx)


# 정해 코드

from itertools import combinations

N = int(input())
S = input()

P = set()

blank = [i for i in range(1, N)]
comb = list(combinations(blank, 2))

for f, s in comb:
	P.add(S[:f])
	P.add(S[f:s])
	P.add(S[s:])

P = sorted(list(P))

result = 0

for f, s in comb:
	temp = 0
	
	temp += P.index(S[:f]) + 1
	temp += P.index(S[f:s]) + 1
	temp += P.index(S[s:]) + 1
	
	result = max(result, temp)

print(result)