import sys; input = sys.stdin.readline

S = input().strip() # 문자 공백 제거 strip. 이것을 하지 않으면 \n까지 카운트 된다(?)
arr = [[0]*26 for _ in range(len(S))]
arr[0][ord(S[0]) - 97] = 1

for i in range(1, len(S)):
    arr[i][ord(S[i]) - 97] = 1
    for j in range(26):
        arr[i][j] += arr[i-1][j]

q = int(input())
result = []
for _ in range(q):
    a = input().split()
    if int(a[1]) > 0:
        result.append(arr[int(a[2])][ord(a[0]) - 97] - arr[int(a[1]) - 1][ord(a[0]) - 97])
    else:
        result.append(arr[int(a[2])][ord(a[0]) - 97])

print("\n".join(map(str,result)))