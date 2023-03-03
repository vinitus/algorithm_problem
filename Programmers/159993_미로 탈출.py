from collections import deque

def solution(maps):
    answer = 0
    start = 0
    visited = [[10000 for _ in range(len(maps[0]) + 2)] for _ in range(len(maps) + 2)]
    
    for y in range(len(maps)):
        maps[y] = ["X"] + list(maps[y]) + ["X"]
        for x in range(len(maps[0])):
            if not start and maps[y][x] == "S":
                start = (y+1,x,0)
    
    maps = [["X" for _ in range(len(maps[0]))]] + maps + [["X" for _ in range(len(maps[0]))]]
    
    d = [(0,1),(0,-1),(-1,0),(1,0)]
    
    q = deque([start])
    lever_position = 0
    
    print(maps, visited)
    while q:
        y,x,time = q.popleft()
        for dy, dx in d:
            ny = y + dy
            nx = x + dx
            if maps[ny][nx] == "X":
                pass
            elif visited[ny][nx] > time + 1:                
                visited[ny][nx] = time + 1
                if maps[ny][nx] == "L":
                    lever_position = (ny,nx,visited[ny][nx])
                    pass
                else:
                    q.append((ny,nx,time+1))
                    
    if not lever_position:
        return -1
    
    visited = [[10000 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    visited[lever_position[0]][lever_position[1]] = lever_position[2]
    
    q = deque([lever_position])
    end_point = 0
    
    while q:
        y,x,time = q.popleft()
        for dy, dx in d:
            ny = y + dy
            nx = x + dx
            if maps[ny][nx] == "X":
                pass
            elif visited[ny][nx] > time + 1:                
                visited[ny][nx] = time + 1
                if maps[ny][nx] == "E":
                    end_point = (ny, nx)
                else:
                    q.append((ny,nx,time+1))
    
    for i in visited:
        print(i)
    
    if not end_point:
        return -1
    else:
        answer = visited[end_point[0]][end_point[1]]
        
    return answer