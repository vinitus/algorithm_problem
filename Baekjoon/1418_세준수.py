N = int(input())
K = int(input())

def sosu(aa,tmp_list):
    a = int(aa**0.5)+1
    standard = 0
    for i in range(a):
        i += 2
        standard = 1
        if aa % i == 0 and aa != i:
            standard = 0
            break
    if standard != 0:
        tmp_list.append(aa)

sosu_list = []
for i in range(2,(N)+10):
    sosu(i,sosu_list)
count = 0
for i in range(N+1,1,-1):
    for j in range(len(sosu_list)-1,0,-1):
        if i % sosu_list[j] == 0 and sosu_list[j] <= K:
            count += 1
            break
print(count)