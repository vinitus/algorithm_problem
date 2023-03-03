def solution(book_time_list):
    answer = 0
    
    total_minute_list = list(0 for i in range(60*24))
    
    for book_time in book_time_list:
        start_m, start_s = map(int,book_time[0].split(":"))
        start_time = start_m * 60 + start_s
        
        end_m, end_s = map(int,book_time[1].split(":"))
        end_time = end_m * 60 + end_s
        
        if end_time + 10 < 60*24:
            end_time += 10
        else:
            end_time = 60*24 - 1
        
        total_minute_list[start_time] += 1
        total_minute_list[end_time] += -1
    
    
    for index in range(1,60*24):
        total_minute_list[index] += total_minute_list[index-1]
    
    answer = max(total_minute_list)
    
    return answer