import sys
sys.stdin = open('input.txt', 'r')
for t in range(1,11):
    V, E = map(int,input().split())
    lst = list(map(int,input().split()))
    lst3 = list([lst[2*i], lst[2*i+1]] for i in range(E))
    lst3.sort()
    lst = []
    lst2 = []
    for i in range(E):
        lst.append(lst3[i][0])
        lst2.append(lst3[i][1])
    for i in range(E):
        if lst[i] not in lst2:
            if lst2[i] not in lst:
                pass
