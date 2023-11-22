def solution(numbers):
    N = len(numbers)
    answer = [-1 for _ in range(N)]
    stack = []
    
    for i in range(N - 1, -1, -1):
        while stack and numbers[i] >= stack[-1]:
            stack.pop()
        if stack:
            answer[i] = stack[-1]
        stack.append(numbers[i])

    return answer