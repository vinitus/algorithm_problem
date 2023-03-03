def solution(id_list, report, k):
    dct = {}
    for i in report:
        id = i.split()
        if id[1] not in dct:
            dct[id[1]] = [id[0]]
        else:
            if id[0] not in dct[id[1]]:
                dct[id[1]].append(id[0])
                
    id_cnt = list(0 for _ in range(len(id_list)))
    for key, value in dct.items():
        if len(value) >= k:
            for id in value:
                id_cnt[id_list.index(id)] += 1
    return id_cnt