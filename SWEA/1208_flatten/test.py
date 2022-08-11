import sys

sys.stdin = open('input.txt','r')

for testcase in range(1,11):
    N = int(input())
    box_lst = list(map(int,input().split()))
    box_lst.sort()          # 정렬하면 처음은 가장 작은 것, 마지막은 가장 큰 것
    for _ in range(N):
        box_lst[-1] -= 1    # 큰거 -1
        box_lst[0] += 1     # 작은거 +1
        box_lst.sort()      # 다시 정렬
    print(f'#{testcase} {box_lst[-1] - box_lst[0]}')    # 높이차는 큰거 - 작은거 = [-1] - [0]