K = int(input())
key = str(input())
col = len(key)//K
tmp = list(key)
key_list = []

for i in range(col):
    tmp_list = []
    if i % 2 == 0:
        for j in range(K):
            tmp_list.append(key[j+K*i])
    else:
        for j in range(K-1,-1,-1):
            tmp_list.append(key[j+K*i])
    key_list.append(tmp_list)
for i in range(K):
    for j in range(col):
        print(key_list[j][i],end='')