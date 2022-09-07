import time

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

M, N = map(int,input().split())
start = time.time()
result_list = []
if M == 1:
    for i in range(N-M):
        i += 2
        sosu(i,result_list)
else:
    for i in range(N-M+1):
        i += M
        sosu(i,result_list)
for i in result_list:
    print(i)
print(time.time()-start)