def solution(board, moves):
    answer = 0
    
    stack = []
    for move in moves:
        move -= 1
        for y in range(len(board)):
            if board[y][move]:
                element = board[y][move]
                board[y][move] = 0
                stack.append(element)
                break
        if len(stack) >= 2:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                answer += 2
                
    return answer