def solution(board):
    answer = 0
    
    OX = [0,0]
    for y in range(3):
        board[y] = list(board[y])
        for x in range(3):
            if board[y][x] == "O":
                OX[0] += 1
            elif board[y][x] == "X":
                OX[1] += 1
                
    # O와 X의 갯수에 대한 계산
    if OX[1] > OX[0]:
        return 0
    if OX[0] > OX[1] + 1:
        return 0
    if OX[0] == 0 and OX[1] == 0:
        return 1
    
    winner = []
    
    # 가로, 세로 빙고 계산
    for i in range(3):
        if board[i][0] != ".":
            for x in range(3):
                if board[i][x] != board[i][0]:
                    break
            else:
                winner.append(board[i][0])
                
        if board[0][i] != ".":
            for y in range(3):
                if board[y][i] != board[0][i]:
                    break
            else:
                winner.append(board[0][i])
    
    # 빙고 계산
    if board[0][0] != ".":
        for i in range(1,3):
            if board[i][i] != board[0][0]:
                break
        else:
            winner.append(board[0][0])        
    
    if board[0][2] != ".":
        for i in range(1,3):
            if board[i][2-i] != board[0][2]:
                break
        else:
            winner.append(board[0][2])
    
    # 규칙에 대한 검사
    if winner:
        if "X" in winner and "O" in winner:
            pass
        else:
            if winner[0] == "O":
                if OX[0] == OX[1] + 1:
                    return 1
            else:
                if OX[0] == OX[1]:
                    return 1
    else:
        if OX[0] == OX[1] + 1 or OX[0] == OX[1]:
            return 1
    return answer