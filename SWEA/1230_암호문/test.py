import sys
sys.stdin = open('input.txt','r')

T = 10
for t in range(1,T+1):
    N = int(input())
    cryto = list(map(int,input().split()))
    order_N = int(input())
    order = []
    tmp = list(input().split())
    tmp2 = []
    for i in tmp:
        if i.isalpha():
            order.append(tmp2)
            tmp2 = []
        tmp2.append(i)
    order.append(tmp2)
    for i in range(1,len(order)):
        if order[i][0] == "I":
            for idx in range(len(order[i])-1,2,-1):
                cryto.insert(int(order[i][1]),order[i][idx])
        elif order[i][0] == "D":
            for _ in range(int(order[i][2])):
                cryto.pop(int(order[i][1]))
        else:
            for idx in range(int(order[i][1])+1,1,-1):
                cryto.append(order[i][idx])
    print(f'#{t}',end=" ")
    for i in range(10):
        print(cryto[i], end=" ")
    print()