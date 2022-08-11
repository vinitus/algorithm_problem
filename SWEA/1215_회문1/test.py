import sys

sys.stdin = open('SWEA/1215_회문1/input.txt','r')

for t in range(1,11):
    N = int(input())
    lst = []
    for _ in range(8):
        lst.append(list(input()))
    count = 0
    for row in lst:
        for start_idx in range(8-N+1):      # 8개의 칸에서 연속으로 N만큼 집을 수 있는 횟수는 8-N, range 특성상 +1
            tmp = ''                        # 회문을 검사하기위한 문자열
            for N_idx in range(N):          # N만큼 계산
                tmp += row[start_idx+N_idx]
            re_tmp = tmp[::-1]              # 거꾸로 슬라이스
            if tmp == re_tmp:
                count += 1
    
    for x in range(8):
        for y in range(8-N+1):
            tmp = ''
            for N_idx in range(N):
                tmp += lst[y+N_idx][x]
            re_tmp = tmp[::-1]
            if tmp == re_tmp:
                count += 1
    
    print(f'#{t} {count}')