def solution(maps):
    answer = []
    
    d = [[0,1],[0,-1],[-1,0],[1,0]]
    history = []
    
    max_y, max_x = len(maps), len(maps[0])
    
    for index in range(max_y):
        maps[index] = list(i for i in maps[index])
    
    for y in range(max_y):
        for x in range(max_x):
            if maps[y][x] != "X":
                stack = [(y,x)]
                can_stay = 0
                can_stay += int(maps[y][x])
                maps[y][x] = "X"
                
                while stack:
                    now_y, now_x = stack.pop()
                    
                    for dy, dx in d:
                        new_y = now_y + dy
                        new_x = now_x + dx
                        if 0 <= new_y < max_y and 0 <= new_x < max_x and maps[new_y][new_x] != "X":
                            can_stay += int(maps[new_y][new_x])
                            maps[new_y][new_x] = "X"
                            stack.append((new_y,new_x))
                            
                answer.append(can_stay)
    
    if not answer:
        answer = [-1]
    else:
        answer.sort()
    
    return answer