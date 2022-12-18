import sys
input = sys.stdin.readline

student = set()
for i in range(30):
    student.add(i+1)

for _ in range(28):
    student.remove(int(input()))

for num in student:
    print(num)