from math import gcd

def alomost(tmp_list):
    result_tmp = tmp_list[0]
    for i in tmp_list:
        result_tmp = (result_tmp * i) // gcd(result_tmp,i)
    return result_tmp

num_list = list(map(int,input().split()))
num_list_copy = num_list[:]
result_list = []

for i in range(5):
    for j in range(0,4):
        num_list = num_list_copy[:]
        del num_list[i]
        del num_list[j]
        result = alomost(num_list)
        result_list.append(result)

print(min(result_list))