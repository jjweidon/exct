T = int(input())
sum = 0
for _ in range(T):
    a, cal, b = input().split()
    a, b = int(a), int(b)
    if cal == '+':
        sum += a + b
    if cal == '-':
        sum += a - b
    if cal == '*':
        sum += a * b
    if cal == '/':
        sum += a // b

print(sum)


# 정해 코드

result = 0
T = int(input())

for i in range(T):
	s = input().split()
	firstNum = int(s[0])
	command = s[1]
	secondNum = int(s[2])
	
	if command == "+":
		result += firstNum + secondNum
	elif command == "-":
		result += firstNum - secondNum
	elif command == "*":
		result += firstNum * secondNum
	else:
		result += firstNum // secondNum

print(result)