N, M = map(int,input().split())
num_list = list(map(int,input().split()))
result_list = []
for m in range(M):
    i, j = map(int,input().split())
    result = 0
    for index in range(i-1,j):
        result += num_list[index]
    result_list.append(result)
for i in result_list:
    print(i)