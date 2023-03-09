import sys
def input():
    return sys.stdin.readline().rstrip()

W, H = map(int,input().split())

miro = [["H" for i in range(W+2)]]
E = 0
R = []

for y in range(H):
    y += 1
    tmp = ["H"] + list(input()) + ["H"]
    for x in range(1, W+1):
        if tmp[x] == "T":
            tmp[x] = 0
            now = (y,x,0)
        elif tmp[x] == "E":
            E = (y,x)
        elif tmp[x] == "R":
            R += (y,x)
        elif tmp[x] == "H":
            H = (y,x)
        else:
            tmp[x] = int(tmp[x])
    miro.append(tmp)

miro.append(["H" for i in range(W+2)])

d = [(-1,0), (1,0), (0,-1), (1,0)]

def check_range(y,x):
    return 0 <= y < H and 0 <= x < W

answer = 0

visited = {f'{y}y{x}x' : 1}

stk = [now[:]]
while stk:
    y,x,cnt = stk.pop()
    print(visited)
    print(y,x)
    if miro[y][x] == "E":
        break
    for dy, dx in d:
        ny = y + dy
        nx = x + dx
        ncnt = cnt + 1
        if miro[y][x] == "E":
            stk.append((ny,nx,ncnt))
            break
        elif miro[ny][nx] not in ["H", "E", "R"]:
            slip = miro[ny][nx]
            while miro[ny][nx] not in ["H", "E", "R"]:
                slip += miro[ny][nx]
                ny = ny + dy
                nx = nx + dx
                ncnt = cnt + 1
            if miro[ny][nx] == "R":
                ncnt += slip
                if visited.get(f'{ny}y{nx}x') and visited[f'{ny}y{nx}x'] > ncnt:
                    stk.append((ny,nx,ncnt))
                    visited[f'{ny}y{nx}x'] = ncnt
                else:
                    if not visited.get(f'{ny}y{nx}x'):
                        visited[f'{ny}y{nx}x'] = ncnt
                        stk.append((ny,nx,ncnt))
            elif miro[ny][nx] == "E":
                ncnt += slip
                visited[f'{ny}y{nx}x'] = ncnt

if (y,x) == E:
    answer = cnt
else:
    answer = -1

print(answer)