N = int(input())
N_list = list(map(int,input().split()))

if max(N_list) == 1:
    sosu = [0]
if max(N_list) == 2:
    sosu = [2]
else:
    sosu = [2]

    for i in range(max(N_list)):
        i += 1
        a=1
        for j in range(i-2):
            j += 2
            if i % j == 0:
                a = 1
                break
            else:
                a = 0
        if a == 0:
            sosu.append(i)
tmp = []
for i in N_list:
    if i in sosu:
        tmp.append(i)
print(len(tmp))