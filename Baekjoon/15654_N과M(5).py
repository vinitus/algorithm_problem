import sys
def input():
    return sys.stdin.readline().rstrip()
N, M = map(int,input().split())
N_lst = list(map(int,input().split()))
N_lst.sort()
subset_lst = []

def subset():
    if len(subset_lst) == M:
        print(' '.join(map(str,subset_lst)))
        return
    
    for n in N_lst:
        if n not in subset_lst:
            subset_lst.append(n)
            subset()
            subset_lst.pop()

subset()