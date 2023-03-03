def solution(numbers):
    answer = [-1 for i in range(len(numbers))]
    stack = [numbers[-1]]
    for i in range(len(numbers)-2, -1, -1):
        while stack and numbers[i] >= stack[-1]:
            stack.pop()
        else:
            if stack:
                answer[i] = stack[-1]
        stack.append(numbers[i])
        
        
    return answer