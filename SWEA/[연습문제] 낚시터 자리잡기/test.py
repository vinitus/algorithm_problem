import sys
sys.stdin = open('sample_input.txt','r')

T = int(input())
for t in range(1,T+1):
    N = int(input())
    lst = list(list(map(int,input().split())) for _ in range(3))
    lst.sort()
    seat = list([0] for _ in range(N))
    for i in range(3):
        idx = lst[i][0]-1
        person = lst[i][1]
        for j in range(-person//2, person//2+(person%2)):
            if 0 <= idx + j < N:
                seat[idx + j][0] += 1

    print(seat)