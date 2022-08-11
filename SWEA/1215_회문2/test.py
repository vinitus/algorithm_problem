import sys
import time

sys.stdin = open('SWEA/1215_회문2/input.txt','r')

for _ in range(1,11):
    t = int(input())
    lst = []
    for i in range(100):
        lst.append(list(input()))
    count = 0
    max_length = 1
    start = time.time()
    for x in range(100):
        for N in range(max_length+1,100):
            for y in range(100-N+1):
                tmp = ''
                for N_idx in range(N):
                    tmp += lst[y+N_idx][x]
                re_tmp = tmp[::-1]
                if tmp == re_tmp:
                    count += 1
                    max_length = N
                    break
                

        for N in range(max_length+1,100):
            for y in range(100-N+1):
                tmp = ''
                for N_idx in range(N):
                    tmp += lst[x][y+N_idx]
                re_tmp = tmp[::-1]
                if tmp == re_tmp:
                    count += 1
                    max_length = N
                    break
    print(time.time() - start)
    print(f'#{t} {count}')