import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
stack = []
rs = []
index = 0

for i in range(1, n + 1):
    if i <= arr[index]:
        rs.append('+')
        stack.append(i)
        while stack and stack[-1] == arr[index]:
            rs.append('-')
            stack.pop()
            index += 1

    if stack and stack[-1] > arr[index]:
        print('NO')
        break

else:
    for x in rs: print(x)