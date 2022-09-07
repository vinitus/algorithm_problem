N = str(input())
N_list = list(N)
N_list.sort(reverse=True)
for i in N_list:
    print(int(i),end='')