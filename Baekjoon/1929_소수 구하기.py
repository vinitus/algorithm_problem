def sosu_cal(a,tmp_list):
    stop_var = 1
    while 1:
        sqrt_tmp = int(a**0.5)+1
        for i in tmp_list:
            if a % i == 0:
                stop_var = 0
                break
            if i >= sqrt_tmp:
                tmp_list.append(a)
                stop_var = 0
                print(a)
                break
        if stop_var == 0:
            break

M, N = map(int,input().split())

sosu_list = [2]
if M <= 2:
    print(2)
    for tmp in range(N-M-1):
        tmp += M+2
        sosu_cal(tmp,sosu_list)
else:
    for tmp in range(N-M):
        tmp += M
        sosu_cal(tmp,sosu_list)