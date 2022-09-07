def hanoi(top_list,count,goal):
    if top_list==1:
        pass
    elif len(top_list[1]) == 0 and len(top_list[2]) == 0:
        if len(top_list[0]) % 2 == 1:
            top_list[2].append(top_list[0].pop(0))
            print(1, 3)
        else:
            top_list[1].append(top_list[0].pop(0))
            print(1,2)
# K = int(input())
K = 3

top_1st = list(range(1,K+3))
top_2nd = []
top_3rd = []
top_total = [top_1st,top_2nd,top_3rd]
print(hanoi(top_total,top_1st,1))