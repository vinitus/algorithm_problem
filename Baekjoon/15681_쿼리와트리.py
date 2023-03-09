import sys
def input():
    return sys.stdin.readline().rstrip()

N, R, Q = map(int,input().split())

no_dir_tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    U, V = map(int,input().split())
    no_dir_tree[U]+= [V]
    no_dir_tree[V]+= [U]

original_tree = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

cnt = 1
stk = [R]
while stk:
    idx = stk.pop()
    visited[idx] = 1
    for tree_ele in no_dir_tree[idx]:
        if not visited[tree_ele]:
            original_tree[idx].append(tree_ele)
            stk.append(tree_ele)

sub_tree_cnt_list = [0 for _ in range(N+1)]

for i in range(1, N+1):
    stk = [i]
    cnt = 0
    while stk:
        idx = stk.pop()
        if sub_tree_cnt_list[idx]:
            cnt += sub_tree_cnt_list[idx]
        else:
            cnt += 1
            for j in original_tree[idx]:
                stk.append(j)
    sub_tree_cnt_list[i] = cnt

for _ in range(Q):
    U = int(input())
    print(sub_tree_cnt_list[U])