while True:
    n = int(input())
    if n == 0:
        break
    word_list = []
    for i in range(n):
        word_list.append(str(input()))
    word_up = word_list[:]
    for i in range(len(word_up)):
        word_up[i] = word_up[i].upper()
    word_up.sort()
    result = 0
    for j in word_list:
        k = j.upper()
        if k == word_up[0]:
            result = word_list.index(j)
            break
    print(word_list[result])