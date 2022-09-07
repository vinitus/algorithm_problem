# for N in range(2147483647):
N = int(input())
N_list = list(str(N))
yes_no = False

for i in range(len(N_list)-1):
    result = 1
    result2 = 1
    for j in range(0,i+1):
        result *= int(N_list[j])
    for j in range(i+1,len(N_list)):
        result2 *= int(N_list[j])
    if result == result2:
        yes_no = True
        break
    else:
        yes_no = False
if yes_no:
    result = "YES"
else:
    result = "NO"

print(result)

    # for i in range(len(str(N))-1):
    #     k = eval('*'.join(str(i) for i in N[:i+1])) # 앞 자리수의 곱
    #     s = eval('*'.join(str(i) for i in N[i+1:])) # 뒤 자리수의 곱
    #     if k == s:
    #         result2 = "YES"
    #         break
    # else:
    #     result2 = "NO"

    # if result != result2:
    #     print(N,end = " ")
    #     break
    # else:
    #     print(N, end = " ")