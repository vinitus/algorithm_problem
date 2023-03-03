def solution(users, emoticons):
    answer = [0,0]
    
    emoticon_price_list = [[0 for _ in range(len(emoticons))] for _ in range(4**len(emoticons))]
    
    sale_percent_list = [10,20,30,40]
    
    while_emoticon_idx = 1
    emoticon_idx = 0
    sale_percent_idx = 0
    emoticon_price_idx = 0
    
    def cal_sub(num):
        return 100-num
    
    while while_emoticon_idx < len(emoticon_price_list):
        emoticon_price_list[emoticon_price_idx][emoticon_idx] = sale_percent_list[sale_percent_idx]
        emoticon_price_idx += 1
        
        if emoticon_price_idx >= len(emoticon_price_list):
            while_emoticon_idx *= 4
            emoticon_price_idx = 0
            emoticon_idx += 1
        if emoticon_price_idx % while_emoticon_idx == 0:
            sale_percent_idx += 1
            sale_percent_idx %= 4
    
    for emoticon_price in emoticon_price_list:
        user_result = [0,0]
        for user in users:
            user_tmp = 0
            for index in range(len(emoticons)):
                if user[0] <= emoticon_price[index]:
                    user_tmp += emoticons[index] // 100 * cal_sub(emoticon_price[index])
            if user_tmp >= user[1]:
                user_result[0] += 1
            else:
                user_result[1] += user_tmp
                
        if answer[0] < user_result[0]:
            answer = user_result[:]
        elif answer[0] == user_result[0] and answer[1] < user_result[1]:
            answer = user_result[:]

    return answer