import sys
import time

sys.stdin = open('SWEA/1215_회문2/input1.txt','r')

for _ in range(1):
    t = int(input())
    lst = []
    for i in range(100):
        lst.append(input())
    count = 0
    max_length = 1
    start = time.time()
    
    row = lst[0]
    print(row)
    for idx in range(100):
        for end in range(99):
            if row[idx] == row[99-idx-end]:
                for move in range(99-idx-end):
                    if row[idx+move] == row[99-idx-end-move]:
                        print(f'{idx+move} : {row[idx+move]}, {99-idx-end-move} : {row[99-idx-end-move]}')
                        pass
                    else:
                        break
                    if idx+move <= 99-idx-end-move:
                        max_length = 99-idx-end-idx
                        break
                    else:
                        break                            
    # print(time.time() - start)   
    
    print(f'#{t} {max_length}')