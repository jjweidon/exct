import re
from itertools import permutations

def operate(num1, op, num2):
    num1 = int(num1)
    num2 = int(num2)
    if op == '+':
        return str(num1+num2)
    elif op == '-':
        return str(num1-num2)
    elif op == '*':
        return str(num1*num2)
    
def express(exp, operators):
    for operator in operators:
        if len(exp) < 3:
            break
        stack = [exp[0], exp[1]]
        for i in range(2, len(exp)):
            stack.append(exp[i])
            if stack[-2] == operator:
                num2 = stack.pop()
                op = stack.pop()
                num1 = stack.pop()
                stack.append(operate(num1, op, num2))
        exp = stack
    return(abs(int(exp[0])))

def solution(expression):
    result = []
    operator = ['+', '-', '*']
    cases = list(permutations(operator, 3))
    exp = re.split(r"(\+|\-|\*)", expression)
    
    for case in cases:
        result.append(express(exp, case))
    
    return max(result)