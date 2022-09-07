N = int(input())
word_list = []
for i in range(50):
    word_list.append([])
for i in range(N):
    input_str = str(input())
    word_list[len(input_str)-1].append(input_str)

for i in word_list:
    if len(i) == 0:
        pass
    else:
        i = list(set(i))
        i.sort()
        for j in i:
            print(j)