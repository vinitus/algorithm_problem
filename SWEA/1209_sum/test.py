import sys

sys.stdin = open('swea/1209_sum/input.txt','r')

for _ in range(1,11):
    testcase = int(input())
    lst = []
    for _ in range(100):
        lst.append(list(map(int,input().split())))
    max = 0
    for x in lst:
        if max < sum(x):            # 가로는 간단히 sum
            max = sum(x)
    sum_dia = 0                     # 대각선을 저장할 변수
    sum_dia_re = 0                  # 대각선을 저장할 변수
    for x in range(100):
        sum_y = 0                   # y축 합을 저장할 sum_y
        for y in range(100):
            sum_y += lst[y][x]      # y축 탐색하며 합
            if y == x:
                sum_dia += lst[y][x]    # x와 y와 같다면 대각선
            if y == 99 - x:
                sum_dia_re += lst[y][x] # y와 99-x와 같다면 역대각선
        if max < sum_y:
            max = sum_y
    if max < sum_dia:
        max = sum_dia
    if max < sum_dia_re:
        max = sum_dia_re
    print(f'#{testcase} {max}')