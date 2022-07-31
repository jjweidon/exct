import sys
input = sys.stdin.readline

N, M = map(int, input().split())

pokemon = {}
for i in range(1,N+1):
    pokemon[i] = input().strip()
nomekop = {v:k for k,v in pokemon.items()}

result = []
for _ in range(M):
    find = input().strip()
    if find.isdigit():
        find = int(find)
        result.append(pokemon.get(find))
    else:
        result.append(nomekop.get(find))

for x in result:
    print(x)