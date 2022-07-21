words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]
tmp_list = []

for idx in range(len(words)):
    if idx == 0:
        continue
    if words[idx][0] != words[idx-1][-1]:
        print(f'{idx+1}번 탈락')
    else:
        if words[idx] not in tmp_list:
            tmp_list.append(words[idx])
        else:
            print(f'{idx+1}번 탈락')