N = int(input())
file_list = []
for i in range(N):
    file_list.append(str(input()))

standard = list(file_list[0])
for i in file_list:
    i_list = list(i)
    for i in range(len(i_list)):
        if i_list[i] != standard[i]:
            standard[i] = "?"

print(''.join(i for i in standard))