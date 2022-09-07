N,M = map(int,input().split())
value_list = []
for i in range(N):
    tmp = list(map(int,input().split()))
    sum_tmp = 0
    sum_list = []
    for j in tmp:
        sum_tmp+=j
        sum_list.append(sum_tmp)
    value_list.append(sum_list)


K = int(input())
for k in range(K):
    result = 0
    x1,y1,x2,y2 = map(int,input().split())
    for x in range(x1-1,x2):
        if y1 == 1:
            result += value_list[x][y2-1]
        else:
            result += value_list[x][y2-1] - value_list[x][y1-2]
    print(result)