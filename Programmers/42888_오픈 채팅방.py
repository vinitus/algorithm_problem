def solution(records):
    answer = []

    nickname_dict = {}
    log_list = []

    for record in records:
        parsing = record.split(" ")
        status, uid, *nickname = parsing
        if status == "Enter":
            nickname_dict[uid] = nickname[0]
            log_list += [("님이 들어왔습니다.", uid)]
        elif status == "Change":
            nickname_dict[uid] = nickname[0]
        else:
            log_list += [("님이 나갔습니다.", uid)]

    for log in log_list:
        status, uid = log
        answer.append(nickname_dict[uid]+status)

    return answer