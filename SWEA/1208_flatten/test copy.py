import sys

sys.stdin = open('swea/1208_flatten/input.txt','r')

def insert_sort(L_list):
    for i in range(1,len(L_list)):
        for j in range(i,0,-1):
            if L_list[j] < L_list[j-1]:
                L_list[j], L_list[j-1] = L_list[j-1], L_list[j]
            else:
                break
    return L_list

for testcase in range(1,11):
    N = int(input())
    box_lst = list(map(int,input().split()))
    box_lst = insert_sort(box_lst)
    for _ in range(N):
        box_lst[-1] -= 1    # 큰거 -1
        box_lst[0] += 1     # 작은거 +1
        box_lst = insert_sort(box_lst)
    print(f'#{testcase} {box_lst[-1] - box_lst[0]}')    # 높이차는 큰거 - 작은거 = [-1] - [0]