import sys
S = sys.stdin.readline().strip()

parti = set()
for i in range(len(S)):
    for j in range(len(S)-i):
        parti.add(S[j:j+1+i])

print(len(parti))