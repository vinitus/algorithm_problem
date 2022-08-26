import sys
sys.stdin = open('sample_input.txt','r')

def judge():
    global o_mok,N
    for y in range(N):
        for x in range(N):
            if o_mok[y][x] == "o":
                for dy, dx in [(0,1),(1,0),(1,1),(-1,1),(1,-1),(-1,-1),(-1,0),(0,-1)]:
                    my, mx = y + dy, x + dx
                    cnt = 1
                    while 0 <= mx < N and 0 <= my < N and o_mok[my][mx] == "o":
                        cnt += 1
                        my += dy
                        mx += dx
                    else:
                        if cnt >= 5:
                            return "YES"
    return "NO"

T = int(input())
for t in range(1,T+1):
    N = int(input())
    o_mok = list(list(input()) for _ in range(N))
    print(f'#{t} {judge()}')