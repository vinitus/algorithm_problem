M = int(input())
N = int(input())
result_list = []
for i in range(int(M**0.5)-1,int(N**0.5)+1):
    if i**2 >= M and i**2 <= N:
        result_list.append(i**2)

if len(result_list) == 0:
    print(-1)
else:
    result = 0
    for i in result_list:
        result += i
    print(result)
    print(min(result_list))